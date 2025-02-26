import requests
import time as clock
import influxdb_client, os, time
import random
from influxdb_client import InfluxDBClient, Point, WritePrecision,WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS

"""
Initial param config for the device pinout
"""
config={
    "pin0": {"measurement":"flujo_agua_granuladora_americano", "tags": {"maquina":"0x01","lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin1": {"measurement":"flujo_agua_granuladora_frances", "tags":{ "maquina":"0x01","lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin2": {"measurement":"vel_giro_olla_americano", "tags":{ "maquina":"0x01","lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin3": {"measurement":"vel_giro_olla_frances", "tags":{ "maquina":"0x01","lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin4": {"measurement":"flujo_combustible_quemador_secador", "tags":{ "maquina":"0x01","lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin5": {"measurement":"presion_combustible_quemador_secador", "tags":{ "maquina":"0x01","lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin6": {"measurement":"temp_camara_combustion", "tags":{  "maquina":"0x01","noSensor":1,"lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin7": {"measurement":"temp_camara_combustion", "tags":{ "maquina":"0x01","noSensor":2,"lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin8": {"measurement":"temp_salida_gases", "tags":{  "maquina":"0x01","lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin9": {"measurement":"frec_vibrador_malla", "tags":{ "maquina":"0x01","lote":0,"noSensor":0,"punto_medicion":0,"ubicacion":1}},
    "pin10": {"measurement":"frec_vibrador_malla", "tags":{ "maquina":"0x01","lote":0,"noSensor":1,"punto_medicion":0,"ubicacion":1}},
    "pin11": {"measurement":"frec_vibrador_malla", "tags":{ "maquina":"0x01","lote":0,"noSensor":2,"punto_medicion":0,"ubicacion":1}},
    "pin12": {"measurement":"frec_vibrador_malla", "tags":{  "maquina":"0x01","lote":0,"noSensor":3,"punto_medicion":0,"ubicacion":1}},
    "pin13": {"measurement":"temp_prod_terminado", "tags":{  "maquina":"0x01","lote":0,"noSensor":0,"punto_medicion":0,"ubicacion":1}},
    "pin14": {"measurement":"pesaje_prod_terminado", "tags":{  "maquina":"0x01","lote":0,"noSensor":0,"punto_medicion":0,"ubicacion":1}},
}

configDev2={
    "pin0": {"measurement":"flujo_agua_granuladora_americano", "tags": {"maquina":"0x02","lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin1": {"measurement":"flujo_agua_granuladora_frances", "tags":{ "maquina":"0x02","lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin2": {"measurement":"vel_giro_olla_americano", "tags":{ "maquina":"0x02","lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin3": {"measurement":"vel_giro_olla_frances", "tags":{ "maquina":"0x02","lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin4": {"measurement":"flujo_combustible_quemador_secador", "tags":{ "maquina":"0x02","lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin5": {"measurement":"presion_combustible_quemador_secador", "tags":{ "maquina":"0x02","lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin6": {"measurement":"temp_camara_combustion", "tags":{  "maquina":"0x02","noSensor":1,"lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin7": {"measurement":"temp_camara_combustion", "tags":{ "maquina":"0x02","noSensor":2,"lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin8": {"measurement":"temp_salida_gases", "tags":{  "maquina":"0x02","lote":0,"punto_medicion":0,"ubicacion":1}},
    "pin9": {"measurement":"frec_vibrador_malla", "tags":{ "maquina":"0x02","lote":0,"noSensor":0,"punto_medicion":0,"ubicacion":1}},
    "pin10": {"measurement":"frec_vibrador_malla", "tags":{ "maquina":"0x02","lote":0,"noSensor":1,"punto_medicion":0,"ubicacion":1}},
    "pin11": {"measurement":"frec_vibrador_malla", "tags":{ "maquina":"0x02","lote":0,"noSensor":2,"punto_medicion":0,"ubicacion":1}},
    "pin12": {"measurement":"frec_vibrador_malla", "tags":{  "maquina":"0x02","lote":0,"noSensor":3,"punto_medicion":0,"ubicacion":1}},
    "pin13": {"measurement":"temp_prod_terminado", "tags":{  "maquina":"0x02","lote":0,"noSensor":0,"punto_medicion":0,"ubicacion":1}},
    "pin14": {"measurement":"pesaje_prod_terminado", "tags":{  "maquina":"0x02","lote":0,"noSensor":0,"punto_medicion":0,"ubicacion":1}},
}

"""
influx db config
"""
token = ("")
org = ""
url = ""
bucket="testdata"
time=int(clock.time())-10000 #add unix time in seconds precission 
points=[]

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org,enable_gzip=True)
write_api = write_client.write_api(write_options=WriteOptions(SYNCHRONOUS,batch_size=100))
for value in range(5000):
    for pin in config.values():
        fields={"val":random.randrange(0, 20)} #add value fields to object
        pin.update(fields=fields,time=time) # merge into current object 
        point = Point.from_dict(pin,WritePrecision.S) # create a influx point with the data, important to include the time precission 
        points.append(point)
        print(point)
        #write_api.write(bucket=bucket, org=org, record=point)
        
    for pin in configDev2.values():
        fields={"val":random.randrange(0, 20)}
        pin.update(fields=fields,time=time)
        point = Point.from_dict(pin,WritePrecision.S)
        points.append(point)
        print(point)
        #write_api.write(bucket=bucket, org=org, record=point)
    time+=1

    if len(points)>=100:
        write_api.write(bucket,org,points)
        points=[]

#write_api.write(bucket, org,points)

import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = ("")
org = ""
url = ""

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket=""

write_api = write_client.write_api(write_options=SYNCHRONOUS)
   
for value in range(5):
    print(value)
    point = (Point("").tag("", "").field("", value) )
    write_api.write(bucket=bucket, org=org, record=point)
    time.sleep(1) # separate points by 1 second


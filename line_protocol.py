import time
import datetime
import random

presentDate = int(time.time())
data=""
for i in range (1000):
    data+="temp,machine="+str(random.randint(10, 100))+" "
    data+='sensorTempCels='+str(random.randint(10, 500))+'i,sensorTempAprox='+str(random.randint(10, 600))+'i,chasisTemp='+str(random.randint(10, 500))+'i '
    data+=str(presentDate+i)+"\n"
    
print(data)

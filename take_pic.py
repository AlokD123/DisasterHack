import paho.mqtt.client as mqtt
import time
import json
from sensor_test import getInput
from picamera import PiCamera
import array

import base64
def on_publish(mosq,user_data,mid):
    pass

solace_url = "mr2aqty0xnecd5.messaging.solace.cloud"
#solace_url = "mqtt.eclipse.org"
solace_port = 21062
solace_user = "solace-cloud-client"
solace_passwd = "80rkel9bt7789ja91pgls7snl"
solace_clientid = "vats_id1"
solace_topic_temp = "devices/camera/events"


client=mqtt.Client(solace_clientid)

client.username_pw_set(solace_user,solace_passwd) 
client._on_publish = on_publish

camera=PiCamera()

client.connect(solace_url,solace_port)

while 1:
	ret = getInput()

	temp,humidity,lat,longitude=ret[0],ret[1],ret[2][0],ret[2][1]
	print(temp, humidity, lat, longitude)

	if float(temp)>0:
	    print("capture")
	    camera.start_preview()
	    time.sleep(1)
	    camera.capture('LastCapture.jpg')
	    camera.stop_preview()
	
	    f=open('LastCapture.jpg','rb')
	    content=f.read()
	    byte_arr=list(content)
	    #byte_arr = base64.b64encode(content)
	    print(type(byte_arr))

	    camera_payload = {"timestamp":int(time.time()), "feature":"camera","Pic":byte_arr} #1
	    #camera_payload = {'timestamp':int(time.time()), 'feature':'Camera', 'Pic': byte_arr}
	    #camera_payload = json.dumps(camera_payload,indent=4) #3
	    #camera_payload = json.JSONEncoder().encode(byte_arr)
	    #client.publish('devices/1/camera/events',camera_payload) #5

	gps = [{"lat":lat,"lng":longitude}]
	gps_payload = gps
	gps_payload = json.dumps(gps_payload)
	if temp>20:
	    client.publish('devices/1/gps/events',gps_payload) #Publish site only if e.g. temperature threshold

	temperature_payload = {"timestamp":int(time.time()),"temperature":temp}
	temperature_payload = json.dumps(temperature_payload,indent=4)
	client.publish('devices/1/temperature/events',temperature_payload)

	humidity_payload = {"timestamp":int(time.time()), "feature":humidity}
	humidity_payload = json.dumps(humidity_payload,indent=4)
	client.publish('devices/1/humidity/events',humidity_payload)

client.loop_forever()

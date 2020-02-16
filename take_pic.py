import paho.mqtt.client as mqtt
import time
import json
import sensor_test
from picamera import PiCamera

def on_publish(mosq,user_data,mid):
    pass

client=mqtt.Client()

client.username_pw_set('','') 
client._on_publish = on_publish

camera=PiCamera()

client.connect('mqtt.eclipse.org',1880)

ret = getInput()

temp,humidity,lat,longitude=ret[0],ret[1],ret[2][0],ret[2][1]
print(temp, humidity, lat, longitude)

if temp>0:
    print("capture")
    camera.start_preview()
    sleep(1)
    camera.capture('LastCapture.jpg')
    camera.stop_preview()

    f=open('LastCapture.jpg','rb')
    content=f.read()
    byte_arr=bytes(content)

    camera_payload = {'timestamp':int(time.time()), 'feature':'Camera', 'Pic': byte_arr}
    camera_payload = json.dumps(camera_payload,indent=4)
    client.publish('devices/camera/events',camera_payload)

client.loop_forever()

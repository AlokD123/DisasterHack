import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import json

# initialize device


# Connection parms for Solace Event Broker
#solace_url = "mr2aqty0xnecd5.messaging.solace.cloud"
solace_url = "mqtt.eclipse.org"
solace_port = 1883
solace_user = "solace-cloud-client"
solace_passwd = "80rkel9bt7789ja91pgls7snl"
solace_clientid = "vats_id"
solace_topic_temp = "devices/temperature/events"
solace_topic_humidity = "devices/humidity/events"
payload = "Hello from Raspberry Pi"


# MQTT Client Connectivity to Solace Event Broker
client = mqtt.Client(solace_clientid)
client.username_pw_set(username=solace_user,password=solace_passwd)
print ("Connecting to solace {}:{} as {}". format(solace_url, solace_port, solace_user))
client.connect(solace_url, port=solace_port)
client.loop_start()

# Publish  Sensor streams to Solace Ebent Broker
while True:
    temp,humidity,latitude,longitude = 1,2,3,4 #Get data here
    #print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)
    # Read  Temp and humidity sensotr outputs
    temp_payload = temp
    hum_payload = humidity
    #print("Streaming sensor events to Solace")
    # Construct JSON sensor output string
    temp_payload = {"timestamp": int(time.time()), "device": "Temperature", "Temperature": temp_payload}
    temp_payload =  json.dumps(temp_payload,indent=4)
    print (temp_payload)
    hum_payload = {"timestamp": int(time.time()), "device": "Humidity", "Humidity": hum_payload}
    hum_payload = json.dumps(hum_payload, indent=4)
    print (hum_payload)
    # Publish Json event to Solace Event Broker
    client.publish(solace_topic_temp, temp_payload, qos=1)
    client.publish(solace_topic_humidity,hum_payload, qos=1)
    time.sleep(1)
client.loop_stop()
client.disconnect()

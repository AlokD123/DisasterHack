'''
  sensor_test.py - This is basic sensor_test example.
  Created by Yasin Kaya (selengalp), August 28, 2018.
'''

from cellulariot import cellulariot
import time
import geocoder

def getInput():
	node = cellulariot.CellularIoTApp()
	node.setupGPIO()

	node.disable()
	time.sleep(1)
	node.enable()

	g = geocoder.ip('me')

	node.turnOnRelay()
	time.sleep(2)
	node.turnOffRelay()
	time.sleep(0.5)

	node.turnOnUserLED()
	time.sleep(2)
	node.turnOffUserLED()

	return [str(node.readTemp()),str(node.readHum()),g.latlng]

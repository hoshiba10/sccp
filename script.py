#!/usr/bin/python
#!/usr/bin/env python
#-*- coding: utf -8 -*-

import sys
import Adafruit_DHT
import commands
import time

from datetime import datetime

sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
'2302': Adafruit_DHT.AM2302 }

if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
	sensor = sensor_args[sys.argv[1]]
	pin = sys.argv[2]
else:
	sys.exit(1)

	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:

	out = open("result.txt", "w")
	out_data = open("data.csv", "a")

	out.writelines("TEST=" + '{0:0.1f}'.format(temperature) + "\n")
	out.writelines("TEST1=" + '{1:0.1f}'.format(temperature.humidity))

	out_data.writelines("\n" + datetime.now().strftime("%Y/%m/%d% %H:%M:%S") + ",")
	out_data.writelines('{1:0.1f}'.format(temperature,humidity))

	out.close()
	out_data.close()
else:
	sys.exit()
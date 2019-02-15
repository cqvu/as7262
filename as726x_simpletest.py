#!/usr/bin/env python3

import time
import datetime

import board
import busio

from adafruit_as726x import Adafruit_AS726x
from PushingBox import PushingBox
pbox = PushingBox()
devid = 'v62C2A5DBACDA4FC'

startTime = time.time()
#maximum value for sensor reading
max_val = 16000

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = Adafruit_AS726x(i2c)

sensor.conversion_mode = sensor.MODE_2

while True:
    # Wait for data to be ready
    while not sensor.data_ready:
        time.sleep(.1)

    print('Violet: ' + str(sensor.violet))
    print('Blue: ' + str(sensor.blue))
    print('Green: ' + str(sensor.green))
    print('Yellow: ' + str(sensor.yellow))
    print('Orange: ' + str(sensor.orange))
    print('Red: ' + str(sensor.red))
    print("\n")
    
    with open('as7262_readings.txt', 'a+') as write_file:
        write_file.write(str(datetime.datetime.now()) + "," + str(sensor.violet) + 
                         "," + str(sensor.blue) + "," + str(sensor.green) + "," +
                         str(sensor.yellow) + "," + str(sensor.orange) + "," + 
                         str(sensor.red) + "\n")
    if sensor.violet != 0 or sensor.blue != 0 or sensor.green != 0 or sensor.yellow != 0 or sensor.orange != 0 or sensor.red != 0: 
        try:
            pbox.push(devid, violetData=sensor.violet, blueData=sensor.blue,
                    greenData=sensor.green, yellowData=sensor.yellow, 
                    orangeData=sensor.orange, redData=sensor.red)
        except:
            with open('error_log.txt', 'a+') as error_file:
                error_file.write(str(datetime.datetime.now()) + " Could not push to PushingBox. Check internet connection.")

    while(time.time() - startTime <= 60):
        time.sleep(1)
    startTime = startTime + 60


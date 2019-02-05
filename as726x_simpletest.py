#!/usr/bin/env python3

import time

import board
import busio

from adafruit_as726x import Adafruit_AS726x
from PushingBox import PushingBox
pbox = PushingBox()
devid = 'vED428DFB43710F0'

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
        write_file.write(str(sensor.blue) + "\n")

    try:
        pbox.push(devid, sensorData=sensor.blue)
    except:
        print("Could not push to PushingBox. Check internet connection.")

    while(time.time() - startTime <= 60):
        time.sleep(1)
    startTime = startTime + 60


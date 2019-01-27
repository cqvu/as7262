#!/usr/bin/env python3

import time

import board
import busio

from adafruit_as726x import Adafruit_AS726x
from PushingBox import PushingBox
pbox = PushingBox()
devid = 'vED428DFB43710F0'

#maximum value for sensor reading
max_val = 16000

#max number of characters in each graph
max_graph = 80

def graph_map(x):
    return min(int(x * max_graph / max_val), max_graph)

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

    pbox.push(devid, sensorData=sensor.blue)
    time.sleep(50)


'''
    #plot plot the data
    print("\n")
    print("V: " + graph_map(sensor.violet)*'=')
    print("B: " + graph_map(sensor.blue)*'=')
    print("G: " + graph_map(sensor.green)*'=')
    print("Y: " + graph_map(sensor.yellow)*'=')
    print("O: " + graph_map(sensor.orange)*'=')
    print("R: " + graph_map(sensor.red)*'=')
'''

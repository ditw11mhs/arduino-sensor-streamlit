# Importing Libraries
from serial import Serial
import serial.rs485
import time

master = Serial(port="COM6", baudrate=115200, timeout=0.1)

while True:

    time.sleep(0.01)

    test = master.readline()
    # master.rts = True

    print(test)

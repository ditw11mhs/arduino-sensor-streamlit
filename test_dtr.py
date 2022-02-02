# Importing Libraries
from serial import Serial
import serial.rs485
import time




# rtscts dsrdtr
master = Serial(port="COM6",baudrate=115200,timeout=0.1)
# while True:S
#     master.dtr = 0
#     master.rts = 0
#     time.sleep(0.001)

print("Test Write")
master.write(b'200')
time.sleep(2)

print("Test read")
master.readline()
time.sleep(2)

print('set DTR false')
master.setDTR(False)
time.sleep(2)

print('set DTR True')
master.setDTR(True)
time.sleep(2)

print('close serial')
master.close()

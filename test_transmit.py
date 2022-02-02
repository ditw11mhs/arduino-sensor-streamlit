# Importing Libraries
from serial import Serial
import serial.rs485
import time

# pc transmit vcc
# default dope
# rtscts nope
# dsrdtr nope
# xonxoff dope

# rtscts dsrdtr
master = Serial(port="COM6", baudrate=115200, timeout=0.1)
time.sleep(1)
# master.rs485_mode = serial.rs485.RS485Settings()
while True:
   
    master.rts = False
    time.sleep(0.001)
    master.write(b"GS1")
    # master.flush()
    time.sleep(0.001)
    master.rts = True
    # time.sleep(0.05)
    
    
    

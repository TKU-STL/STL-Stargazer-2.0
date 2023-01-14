import sys
import socket
import serial
#import serial.threaded
import time

# Open a serial port
ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

# Read a line and send it to the client
line = ser.readline()
print(line)
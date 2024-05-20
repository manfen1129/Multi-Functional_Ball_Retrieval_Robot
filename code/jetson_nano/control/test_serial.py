# /dev/ttyACM0 port of arduino
import time
import serial.tools.list_ports

# get serialport list
port_list = list(serial.tools.list_ports.comports())
print(port_list)
if len(port_list) == 0:
    print("none")
else:
    for i in range(0, len(port_list)):
        print(port_list[i])


portName = "/dev/ttyACM0"
baudRate = 9600
timeOut = 100
Arduino = serial.Serial(portName, baudRate, timeout=timeOut)  # ARDUINO串口
while True:
    Arduino.write(b"w")
    time.sleep(0.001)

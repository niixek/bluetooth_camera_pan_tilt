import serial
from time import sleep

bluetoothSerial = serial.Serial("/dev/rfcomm1", baudrate = 9600)

count = None
while count == None:
    try:
        count = int(raw_input("how much blink u want? the L")
    except:
        pass

bluetoothSerial.write(str(count))
print bluetoothSerial.readline()

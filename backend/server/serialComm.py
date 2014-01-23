import serial

output = serial.Serial("/dev/ttyACM0", 9600)
while True:
    print output.readline()

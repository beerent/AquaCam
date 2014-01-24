import serial

#output = serial.Serial("/dev/ttyACM1", 9600)
output = serial.Serial("/dev/ttyACM0", 9600)
while True:
    input = output.readline()
    print input

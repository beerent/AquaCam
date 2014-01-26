import timeMaster
import socket
import time

#globals
serverSocket = None
client = None;
address = None;

#an easy way to print with the "[SERVER]" prefix.
def report(str):
    print("[SERVER] " + str)


#sets the server socket for the server
#waits for connection from arduino hardware on 
#port 5678
def setConnection():
    #from socket import *
    global serverSocket
    global client
    global address

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(("localhost", 5678))
    serverSocket.listen(5)
    report("waiting for connection from arduino...")
    client, address = serverSocket.accept()

    report("connected to device.")
    
def sender(str):
    global serverSocket
    global client
    global address
    report("sending: " + str)
    serverSocket.send(str)

def reader():
    global serverSocket
    global client
    global address

    while 1:
        data = client.recv(512)

        if data:
            report ("received: " + data)
            return data
        else:
            report("no data yet...")
            time.sleep(3)
    
#handles the string input from the arduino. Reads the first String 
# op 0 = time request
# op 1 = 
def inputHandler(str):
    if str == None:
        report("no input")
        return 
    input = list(str)
    #assuming there are no two digit opcodes
    op = int(input[0])
    if op == 0:
        sender(getTimeString())
    else:
        print("no op for: " + op + " in string: " + str)


#function manages the lights, turning them on or off
#light corresponds to the specific light, mode corresponds to the 
#light turning on or off.

#codes:
#0: light 1 29 gal.
#1: light 2 29 gal.
#2: heater 29 gal.
#3: OPEN 

#4: light 1 10 gal.
#5: light 2 10 gal.
#6:  heater 10 gal.
#7: OPEN
def relayManager(pin, mode):
    level, ob;
    if mode == 1:
        ob = "HIGH"
    else:
        ob = "LOW"

def runServer():
    setConnection()

    while True:
        inputHandler(reader())
        break

#run the server
runServer()

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

#null all connections to the Socket
def nullConn():
    global serverSocket
    global client
    global address
    serverSocket = None
    client = None
    address = None
#sets the server socket for the server
#waits for connection from arduino hardware on 
#port 5678
def setConnection():
    global serverSocket

    host = ''
    port = 5678
    addres = (host, port)

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((addres))
    serverSocket.listen(5)

    report("Listening for connection ...")

    
def sender(str):
    global client
    client.send(str)
    report("sent: " + str);

def reader():
    global serverSocket
    global client
    global address

    while 1:
        data = client.recv(512)

        #wait for a request
        if data:
            report ("received: " + data)
            return data
    
#handles the string input from the arduino. Reads the first String 

#arduino ops
# op 0 = time request
# op 1 = 

# admin ops
# op -1 = terminate server

def inputHandler(str):
    if str == None:
        report("no input")
        return 

    input = str.split()
    #assuming there are no two digit opcodes
    try:
        op = int(input[0])
        if op == 0: #time request
            sender(timeMaster.getTimeString())
        elif op == 1: #status request
            statusRequest()
        else:
            report("no op for: " + input[0] + " in string: " + str)

    except: 
        report(input[0]  + " is not a valid op code")

#function manages the lights, turning them on or off
#light corresponds to the specific light, mode corresponds to the 
#light turning on or off.
def relayManager(pin, mode):
    level, ob;
    if mode == 1:
        ob = "HIGH"
    else:
        ob = "LOW"

#submit status update from arduino to file
def statusRequest():
    status = "| " + timeMaster.getTimeString() + " | " + reader() + " |"
    with open("arduinoStatus.txt", "a") as file:
        file.write(status)

def runServer():
    global serverSocket
    global client
    global address

    setConnection()
    
    while True:
        client, address = serverSocket.accept()

        print "Connected to client at ", address
        inputHandler(reader())
        client.close()

    #setConnection()

    #while True:
        
    #    report("waiting for connection from arduino...")
    #    client, address = serverSocket.accept()
    #    report("connected to device.")

    #    inputHandler(reader())
    #    client.close()

#run the server
runServer()

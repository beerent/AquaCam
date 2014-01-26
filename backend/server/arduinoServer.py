import timeMaster

#an easy way to print with the "[SERVER]" prefix.
def report(str):
    print("[SERVER] " + str)


#sets the server socket for the server
#waits for connection from arduino hardware on 
#port 5678
def setConnection():
    import socket

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 5678))
    serversocket.listen(5)
    report('waiting for connection...')
    
    conn, addr = serversocket.accept()
    report( "connection made by " + addr)

#def sender(str):
    
#def reader(str):
    
#handles the string input from the arduino. Reads the first String 
# op 0 = time request
# op 1 = 
def inputHandler(str):
    input = list(str)
    #assuming there are no two digit opcodes
    op = input[0]
    if op == 0:
        sender(getTimeString())


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
    while True:
        handleInput(reader())
print timeMaster.getTimeString()

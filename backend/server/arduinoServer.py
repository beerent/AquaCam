#an easy way to print with the "[SERVER]" prefix.
def report(str){
    print("[SERVER] " + str)
}

#sets the server socket for the server
#waits for connection from arduino hardware on 
#port 5678
def setConnection(){
    import socket

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 5678))
    serversocket.listen(5)
    report('waiting for connection...')
    
    conn, addr = serversocket.accept()
    report( "connection made by " + addr)
}

#handles the string input from the arduino
def inputHandler(str){
    
}

#function manages the lights, turning them on or off
#light corresponds to the specific light, mode corresponds to the 
#light turning on or off.
def lightManager(light, mode){

}


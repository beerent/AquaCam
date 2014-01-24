import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 5678))
serversocket.listen(5)
print 'waiting...'
    
conn, addr = serversocket.accept()
print "connection made by", addr

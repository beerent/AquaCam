import socket

s = socket.socket()
s.connect((socket.gethostname(), 1234))
data = s.recv(512)
print(data)
s.send("0 aquarium active 'Y' aquarium_name 'test'")
data = s.recv(512)
print(data)
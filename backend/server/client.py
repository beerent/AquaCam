import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 5678))

s.send("0 1 2 \n")
data = s.recv(512)
print("got: " + data)

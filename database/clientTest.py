import socket

s = socket.socket()
s.connect((socket.gethostname(), 1234))
data = s.recv(512)
print(data)
s.send("update aquarium active N aquarium_name test")
data = s.recv(512)
print(data)

#insert: insert 

#update: table value_to_change desired_change record_to_change actual_record_value
   # ex: update aquarium active N aquarium_name riley1
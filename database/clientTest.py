import socket

def report(str):
	print("[CLIENT] " + str)

s = socket.socket()
s.connect((socket.gethostname(), 1234))
data = s.recv(512)
report(data)
s.send("update active N aquarium_name test")
data = s.recv(512)
report(data)

#insert: insert 

#update: table value_to_change desired_change record_to_change actual_record_value
   # ex: update active N aquarium_name riley1
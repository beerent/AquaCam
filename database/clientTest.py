import socket

def report(str):
	print("[CLIENT] " + str)

s = socket.socket()
s.connect((socket.gethostname(), 1234))
data = s.recv(512)
report(data)
s.send("1 \"1200AM\" \"tank1\" \"79.3\"")
data = s.recv(512)
report(data)

s.send("2 \"1\" \"1200AM\" \"Y\"")
data = s.recv(512);
report(data)
s.send("0") # terminate connection

#insert: insert 

#update: table value_to_change desired_change record_to_change actual_record_value
   # ex: update active N aquarium_name riley1

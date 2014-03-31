import socket

def report(str):
	print("[CLIENT] " + str)

s = socket.socket()

s.connect((socket.gethostname(), 5678)) # connect

data = s.recv(512) #receive 1
report("A: " + data)

s.send("1") #send op code 1, history database insertion

data = s.recv(512) #reveive 1
report("B: " + data)

s.send("1 \"1200AM\" \"tank1\" \"79.3\"") #send data part (1/2)

report("send 2B")

data = s.recv(512) #receive 1
report("C: " + data)

s.send("2 \"1\" \"1200AM\" \"Y\"") #send data part (2/2)
report("send 2c")

data = s.recv(512); #receive 1
report("D: " + data)

#insert: insert 

#update: table value_to_change desired_change record_to_change actual_record_value
   # ex: update active N aquarium_name riley1
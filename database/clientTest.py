import socket

def report(str):
	print("[CLIENT] " + str)

def insertTemp():
	s = socket.socket()
	s.connect(('', 5678))
	data = s.recv(512);
	report("A")
	s.send("1 \"1200AM\" \"tank1\" \"79.3\"")
	report("B")
	data = s.recv(512)
	report("C")
	s.close()

def insertLight():
	s = socket.socket()
	s.connect(('', 5678))
	data = s.recv(512);
	report("A")
	s.send("2 \"1\" \"1200PM\" \"Y\" \"tank1\"")
	report("B")
	data = s.recv(512)
	report("C")
	s.close()

def insertImg():
	s = socket.socket()
	s.connect(('', 5678))
	data = s.recv(512);
	report("A")
	s.send("3")
	report("B")
	data = s.recv(512)
	report("C")
	s.close()

insertTemp()
insertLight()
insertImg()
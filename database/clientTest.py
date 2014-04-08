import socket

def report(str):
	print("[CLIENT] " + str)

def insertTemp():
	s = socket.socket()
	s.connect(('', 5677))
	data = s.recv(512);
	report("A")
	s.send("A")
	data = s.recv(512)
	report("B")
	s.send("1 \"1200AM\" \"tank1\" \"79.3\"")
	report("C")
	data = s.recv(512)
	report("D")
	s.close()

def insertLight():
	s = socket.socket()
	s.connect(('', 5677))
	data = s.recv(512);
	report("A")
	s.send("A")
	data = s.recv(512)
	report("B")
	s.send("2 \"1\" \"1200PM\" \"Y\" \"tank1\" \"riley\"")
	report("C")
	data = s.recv(512)
	report("D")
	s.close()

def insertImg():
	s = socket.socket()
	s.connect(('', 5677))
	data = s.recv(512);
	s.send("A")
	report("A")
	data = s.recv(512)
	report("B")
	s.send("3 \"tank1\" \"riley\" \"1240\"")
	report("C")
	data = s.recv(512)
	report("D")
	s.close()

def universalUpdate():
	s = socket.socket()
	s.connect(('', 5677))
	data = s.recv(512)
	report("A")
	s.send("A")
	data = s.recv(512)
	s.send("4")
	report("B")
	data = s.recv(512)
	report("C")
	s.close()

insertTemp()
insertLight()
insertImg()
universalUpdate()
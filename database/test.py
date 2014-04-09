import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def runServer():
	serverSocket.bind(('', 5677))
	serverSocket.listen(5)
	print("Listening for connection ...")
	while 1:
		clientSock, ad = serverSocket.accept()
		ip = ad
		print ("connection made")
		data = clientSock.recv(512);
		print data;
		#thread.start_new_thread(clientHandler, (clientSock,))

runServer()
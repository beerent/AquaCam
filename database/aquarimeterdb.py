import MySQLdb
import socket
import thread
import sys

import pygame.camera
import pygame.image

#***** server var's *****#
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#global var of the database
host = 'localhost';
user = 'root'
password = 'cuse1234'
database_name = 'aquarameter'

#global camera object. starts as None
cam = None

#database: connected to aquarameter mysql 
database = MySQLdb.connect(host, user, password, database_name)

arduinoUpdateBit = -1

#called when program starts to initialize the camera for further uses.
def cameraInit():
	global cam
	pygame.camera.init()
	cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
	cam.start()

# used to print statements, appending "[SERVER]" to the front
def report(str):
	print("[SERVER] " + str)

def arduinoRequest(op):
	global arduinoUpdateBit
	arduinoUpdateBit = 1
	report("arduinoUpdateBit set to 1")
	return 1;

#returns a cursor for the current database
def getCursor():
    return database.cursor()

#executes a command that is passed in to the database
#returns 1 if successful, else returns -1
def execute(sqlCommand):
	if sqlCommand == "null":
		return "-1";
	cursor = getCursor()
	try:
		cursor.execute(sqlCommand)
		database.commit()
		report("database committed")
		return 1;
	except:
		database.rollback()
		report("database fail")
		return "-1"

#accepts an array of string as a paramater
#depending on the desired operation, the strings in the
#array are plugged in accordingly.
def sendSQL(data):
	global count
	cmd = 'null'

	if data[0] == "1":
		id = 0;
		cmd = "insert into temp_history values (" + data[1] + ", " + data[2]+", " + data[3] + ", curdate(), " + str(id) + ")"
		print(cmd)
	# light_number, date, time, power
	elif data[0] == "2":
		id = 9
		cmd = "insert into light_history values (" + data[1] + ",  curdate(), " + data[2]+", " + data[3] + ", " + data[4] + ", " + data[5] + ", " + str(id) + ")"
		print(cmd)
	elif data[0] == "3":
		id = 0
		img_path = "/var/www/images/" + data[2][1:len(data[2])-1] + "/" + data[1][1:len(data[1])-1] + "/test.jpg"
		
		#needs to call three times to get current photo.
		#not sure why. must have a buffer.
		img = cam.get_image()
		img = cam.get_image()
		img = cam.get_image()
		pygame.image.save(img, img_path)
		pygame.camera.quit()
		cmd = "insert into img_history values (" + str(id) + ", \"" + img_path + "\", " + data[1]+", " + data[2] + ", curdate(), " + data[3] + ")";
		print(cmd)
	else:
		print(data)
		return "-1";
	return execute(cmd);

'''
def opHandler(clientSock, op):
	clientSock.send("1")
	if(op == "1"): #insert request
		for x in range(0, 2):
			input = clientSock.recv(1024)
			data = input.split()
			complete = insertSQL(data)
			clientSock.send(str(complete)) 
'''

# accepts a socket connected to a client
# sends the client "1" to tell them we are ready
# for their data. accepts data, then reports back 
# "1" if their command was successful, or -1 otherwise
def clientHandler(clientSock):
	global arduinoUpdateBit
	clientSock.send("1") #ready for input
	client = clientSock.recv(1024) # determine who client is
	report("client = " + client)
	
	if client == "A":
		if arduinoUpdateBit == 1: #we need a UNI update
			arduinoUpdateBit = 0; 
			report("arduinoUpdateBit set to 0")
			clientSock.send("2"); #2 tells arduino we need UNI update
			input = clientSock.recv(1024) #duino says she understands
			return
		
	clientSock.send("1") #tell duino client we are ready for input
	input = clientSock.recv(1024)
	data = input.split()
		
	if(data[0] == "-1"): #arduino is just checking for requests
		cliendSock.send(str(arduinoUpdateBit))
	elif(int(data[0]) in range(0,4)): #arduino has an insert request
		complete = sendSQL(data)		
	elif(int(data[0]) == 4): #php has an arduino request
		report("found 4")
		complete = arduinoRequest(0)
	else:
		clientSock.send("-1")
		return

	clientSock.send(str(complete))
	#report("connection closed.")
	#clientSock.close()

# listens for clients forever. Upon a connection, 
# clientHandler is called, passing in the socket connected
# to the client 
def runServer():
	serverSocket.bind(('', 5677))
	serverSocket.listen(5)
	report("Listening for connection ...")
	while 1:
		clientSock, ad = serverSocket.accept()
		ip = ad
		report ("connection made")
		thread.start_new_thread(clientHandler, (clientSock,))
	
# prints the possible options and runs what the user selects
# can also pass in an argument to skip the foreplay 	
def menu():
	cameraInit()
	arduinoUpdateBit = 0
	if len(sys.argv) > 1:
		command = sys.argv[1]
	else:
		report("what would you like to do?")
		report("1: run server")
		command = raw_input('--> ')
	
	if command == '1':
		runServer()

#begin server
menu() 

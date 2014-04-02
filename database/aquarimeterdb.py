import MySQLdb
import socket
import thread
import sys

#***** server var's *****#
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#global var of the database
host = 'localhost';
user = 'root'
password = 'cuse1234'
database_name = 'aquarameter'

#database: connected to aquarameter mysql 
database = MySQLdb.connect(host, user, password, database_name)

# used to print statements, appending "[SERVER]" to the front
def report(str):
	print("[SERVER] " + str)

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
	cmd = 'null'
	# insert to history tables
	# time, aquarium_name, temperature, date
	if data[0] == "1":
		id = 0;
		cmd = "insert into temp_history values (" + data[1] + ", " + data[2]+", " + data[3] + ", curdate(), " + str(id) + ")"
		print(cmd)
	# light_number, date, time, power
	elif data[0] == "2":
		cmd = "insert into light_history values (" + data[1] + ",  curdate(), " + data[2]+", " + data[3] + ", " + data[4] + ")"
		print(cmd)
	elif data[0] == "3":
		id = 0;
		img_path = "null"
		cmd = "insert into img_history values (" + str(id) + ", " + img_path + ")"
		print(cmd)
	else:
		print(data)
		return "-1";
	return execute(cmd);

def opHandler(clientSock, op):
	clientSock.send("1")
	if(op == "1"): #insert request
		for x in range(0, 2):
			input = clientSock.recv(1024)
			data = input.split()
			complete = insertSQL(data)
			clientSock.send(str(complete)) 


# accepts a socket connected to a client
# sends the client "1" to tell them we are ready
# for their data. accepts data, then reports back 
# "1" if their command was successful, or -1 otherwise
def clientHandler(clientSock):
	clientSock.send("1") #tell client we are ready for input
	input = clientSock.recv(1024)
	data = input.split()
	complete = sendSQL(data)
	clientSock.send(str(complete))
	#report("connection closed.")
	#clientSock.close()

# listens for clients forever. Upon a connection, 
# clientHandler is called, passing in the socket connected
# to the client 
def runServer():
	serverSocket.bind(('', 5678))
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
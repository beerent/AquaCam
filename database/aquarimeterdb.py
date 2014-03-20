import MySQLdb
import socket
import thread
import sys

#***** server var's *****#

#serverSock: server's socket
serverSock = socket.socket()
serverSock.bind((socket.gethostname(), 1234))

#global var of the database
host = 'localhost';
user = 'root'
password = 'cuse1234'
database_name = 'aquarimeter'

#database: connected to aquarimeter mysql 
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
def updateSQL(data):
	cmd = ''
	if data[0] == 'insert':
		#fix this
		cmd = """ insert into aquarium (data[1], data[2]) values (data[3], data[4])"""
	elif data[0] == 'update':
		cmd = (" update aquarium set " + data[1] + " = '%c' where " + data[3] + " = '%s'") %  (data[2], data[4])
	else:
		report(data[0])
	return execute(cmd)

#data format: (Table | row | name | value)
#op's: 0 - table 
#ex: "Light Light1 ON"
def clientHandler(clientSock):
	clientSock.send("1") #tell client we are ready for input
	input = clientSock.recv(1024) #get data from client
	if "drop" in input:
		report("command contains 'drop', will not continue.")
		clientSock.send("-1")
	else:
		data = input.split()
		complete = updateSQL(data)
		clientSock.send(str(complete)) #can now terminate connection.

# listens for clients forever. Upon a connection, 
# clientHandler is called, passing in the socket connected
# to the client 
def runServer():
	serverSock.listen(5)
	report("waiting for connection...")
	while 1:
		clientSock, address = serverSock.accept()
		report ("connection made")
		thread.start_new_thread(clientHandler, (clientSock,))
	
# prints the possible options and runs what the user selects
# can also pass in an argument to skip the foreplay 	
def menu():
	if len(sys.argv) > 0:
		command = sys.argv[1]
	else:
		report("what would you like to do?")
		report("1: run server")
		command = raw_input('--> ')
	
	if command == '1':
		runServer()
menu()
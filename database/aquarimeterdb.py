import MySQLdb
import socket
import thread

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

#returns a cursor for the current database
def getCursor():
    return database.cursor()

#executes a command that is passed in to the database
def execute(sqlCommand):
	cursor = getCursor()
	sql = sqlCommand
	try:
		cursor.execute(sql)
		database.commit()
		print("database committed")
	except:
		database.rollback()
		print("database fail")

	

def menu():
    print("what would you like to do?")
    print("1: execute SQL command.")
    input = raw_input()
    if(input == "1"):
        print("enter command")
        execute(raw_input())

#accepts an array of string as a paramater
#depending on the desired operation, the strings in the
#array are plugged in accordingly.
def updateSQL(data):
	cmd = ''
	print(data)
	if data[0] == 'insert':
		cmd = """ insert into aquarium (data[1], data[2]) values (data[3], data[4])"""
	elif data[0] == 'update':
		cmd = (" update " + data[1] + " set " + data[2] + " = '%c' where " + data[4] + " = '%s'") %  (data[3], data[5])
	else:
		print(data[0])
	execute(cmd)

#data format: (Table | row | name | value)
#op's: 0 - table 
#ex: "Light Light1 ON"
def clientHandler(clientSock):
	clientSock.send("1") #tell client we are ready for input
	input = clientSock.recv(1024) #get data from client
	clientSock.send("1") #can now terminate connection.
	data = input.split()
	updateSQL(data) 
	#print data

# listens for clients forever. Upon a connection, 
# clientHandler is called, passing in the socket connected
# to the client 
def runServer():
	serverSock.listen(5)
	print("wainting for connection...")
	while 1:
		clientSock, address = serverSock.accept()
		print ("connection made")
		thread.start_new_thread(clientHandler, (clientSock,))
#menu()
runServer()
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
    return db.cursor()

#executes a command that is passed in to the database
def execute(sqlCommand):
    try:
        cursor.execute(sqlCommand)
        database.commit()
    except:
        database.rollback()

def menu():
    print("what would you like to do?")
    print("1: execute SQL command.")
    input = raw_input()
    if(input == "1"):
        print("enter command")
        execute(raw_input())

def updateSQL(data):
	cmd = ''
	if data[0] == 0:
		cmd = "update " + data[1] + " set " + data[2] + "=" + data[3] + " where " + data[4] + "=" + data[5]
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


def runServer():
	serverSock.listen(5)
	print("wainting for connection...")
	while 1:
		clientSock, address = serverSock.accept()
		print ("connection made")
		thread.start_new_thread(clientHandler, (clientSock,))
#menu()
runServer()
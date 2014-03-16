import MySQLdb
import socket

#server setup
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind((socket.gethostname(), 6666))

#global var of the database
host = 'localhost';
user = 'root'
password = 'cuse1234'
database_name = 'aquarimeter'

database = MySQLdb.connect(host, user, password, database_name)

#returns a cursor for the current database
def getCursor():
    return db.cursor()

def execute(sqlCommand):
    if sqlCommand.find("drop") > -1:
        print("attempting to make a drop, continue?")
        input = raw_input()
        if input != "y":
            return;
    
    sql = sqlCommand
    try:
        cursor.execute(sql)
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

def runServer():
	serverSock.listen(5)
	print("wainting for connection...")
	while 1:
		(clientSock, address) = serverSock.accept()
		ct = client_thread(clientSock)
		print("connection made.")

#menu()
runServer()
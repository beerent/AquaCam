import MySQLdb

#global var of the database
host = 'localhost';
user = 'root'
password = 'arcland'
database_name = 'aquarameter'

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

#menu()







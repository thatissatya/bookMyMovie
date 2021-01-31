import mysql.connector


#creating database for application
def dbCreate(): 

    try :

        #establishing the connection to database
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd = 'admin')
        my_cursor = mydb.cursor()

        #performing query for database creation
        my_cursor.execute(" CREATE DATABASE bookmymovie")
        print("Database base created successfull ")
        my_cursor.close()
        mydb.close()

    except :
        print("Failed to connect to database/ database already exist ")



#creating tables for application incase it is not already in database
def tableCreate():

    my_cursor = ''
    try :
        #establish connection to mysql and use database 'bookmymovie'
        mydb = mysql.connector.connect(host = 'localhost', user = 'satya', passwd = 'admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print('database doesnot exist')
        return 
    
    try :
        #table for admin credentials
        my_cursor.execute("CREATE TABLE admin(email varchar(50) PRIMARY KEY, mobile BIGINT(10), password varchar(10), security_key INT(4))")

    except :
        print('admin table already exist')

    try :
        #table for user credentials
        my_cursor.execute("CREATE TABLE user(email varchar(50) PRIMARY KEY, mobile BIGINT(10), password varchar(10), security_key INT(4))")
        
    except:
        print('users table already exist')
    
    try :
        #table for movies show 
        my_cursor.execute("CREATE TABLE movies(id INTEGER AUTO_INCREMENT, email varchar(50) PRIMARY KEY, password varchar(10), security_key int)")
       
    except :
        print('show table already exist')
        


def createShow():
    
    my_cursor = ''

    #establish connection to mysql database and use table movies
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'movies')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist
        ")

def updateShow():
    pass

def deleteShow():
    pass
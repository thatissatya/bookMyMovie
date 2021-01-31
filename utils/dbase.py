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
        my_cursor.execute("CREATE TABLE movies(id INTEGER AUTO_INCREMENT, movie_name VARCHAR(30),city VARCHAR(20), show_time VARCHAR(8), expire_date VARCHAR(10), available_seat INT DEFAULT 120)")
       
    except :
        print('show table already exist')
        


def createShow(moviename, city, showtime, expiredate, availableseat):
    
    my_cursor = ''
    moviename = '"' + moviename +'"'
    city = '"' + city +'"'
    showtime =  '"' + showtime +'"'
    expiredate = '"' + expiredate +'"'
    record = (moviename, city, showtime,expiredate,availableseat)

    sqlinsert = "INSERT INTO movies(movie_name, city, show_time, expire_date, availabe_seat) VALUES(%s, %s, %s, %s, %s)"
    #establish connection to mysql database and use table movies
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'movies')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")
    
    try :
        my_cursor.execute(sqlinsert, record)
        print("Show Created Successful")
    except :
        print("Failed to add new show")


def updateShow():
    pass

def deleteShow(movieName, cityName):
    sqldelete = "DELETE FROM movies WHERE movie_name = movieName AND city = cityName "
    
    my_cursor = ''
    
    #establish connection to mysql database and use table movies
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'movies')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")

    try :
        my_cursor.execute(sqldelete)
        print("Movie Delete Successfully")
    except :
        print("Movies does not exist in the current show list")
    

def deleteAccount(email, password):
    my_cursor = ''
    email = '"' + email +'"'
    password = '"' + password +'"'
    record = (email, password)
    #sql query for accoundt deletion
    sqlaccounddelete = "DELETE FROM users WHERE email = %s and password = %s"

    #establish connection to mysql database and use table movies
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'movies')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")
    
    try :

        my_cursor.execute(sqlaccounddelete, record)
        print("Your account has been deleted permanently")

    except :
        print("Account does not exist/ failed")


def changeAccountPassword(email, passwrod, newpassword):
    pass


def displayShow():

    my_cursor.execute("SELECT * FROM users")
    result = my_cursor.fetchall()
    print("NAME\tEMAIL\t\t\tAGE\tID")
    print("----\t-----\t\t\t---\t---")
    for row in result:
	    print(row[0] + "\t%s" %row[1] + "\t\t%s" %row[2] + "\t%s" %row[3])

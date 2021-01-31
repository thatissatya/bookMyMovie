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
        print("database already exist or Failed to connect to database ")



#creating tables for application incase it is not already in database
def tableCreate():

    my_cursor = ''
    mydb = ''


    try :
        #establish connection to mysql and use database 'bookmymovie'
        mydb = mysql.connector.connect(host = 'localhost', user = 'satya', passwd = 'admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print('database doesnot exist')
        return 
    
    try :
        #table for admin credentials
        my_cursor.execute("CREATE TABLE admin(email VARCHAR(50) PRIMARY KEY, mobile VARCHAR(10), password VARCHAR(10), security_key VARCHAR(4))")

    except :
        print('admin table already exist')

    try :
        #table for user credentials
        my_cursor.execute("CREATE TABLE user(email VARCHAR(50) PRIMARY KEY, mobile VARCHAR(10), password VARCHAR(10), security_key VARCHAR(4))")
        
    except:
        print('users table already exist')
    
    try :
        #table for movies show 
        my_cursor.execute("CREATE TABLE movies(movie_name VARCHAR(30),city VARCHAR(20), show_time VARCHAR(8), expire_date VARCHAR(10), available_seat INT)")
       
    except :
        print('show table already exist')

    #table for specific user booked show
    try :
        my_cursor.execute("CREATE TABLE mybooking(email VARCHAR(50), movie_name VARCHAR(30), city VARCHAR(20), show_time VARCHAR(8), totalseat INT)")

    except:
        print("myshow table already exist ")
    
    my_cursor.close()
    mydb.close()
        


def createShow(moviename, city, showtime, expiredate, availableseat):
    
    my_cursor = ''
    mydb = ''


    moviename = '"' + moviename +'"'
    city = '"' + city +'"'
    showtime =  '"' + showtime +'"'
    expiredate = '"' + expiredate +'"'


    record = (moviename, city, showtime,expiredate,availableseat)

    sqlinsert = "INSERT INTO movies(movie_name, city, show_time, expire_date, availabe_seat) VALUES(%s, %s, %s, %s, %s)"
    #establish connection to mysql database and use table movies
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")
    
    try :
        my_cursor.execute(sqlinsert, record)
        mydb.commit()
        print("Show Created Successful")
    except :
        print("Failed to add new show")

    my_cursor.close()
    mydb.close()


def updateShow(moviename, showtime, expiredate):

    my_cursor = ''
    mydb = ''

    newpassword = '"' + showtime + '"'
    email = '"' + expiredate + '"'
    moviename = '"' + moviename + '"'

    # sql query to update the password
    sqlupdate ='"' + "UPDATE user SET show_time = " + showtime +", " + " expire_date = "+ expiredate + " WHERE email = " + moviename
    
    # establish database connectivity

    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")

    #updating the password
    try :
        my_cursor.execute(sqlupdate)
        mydb.commit()
        print("show update successful")
    except :
        print("Failed to update the show")
    
    #closing connection from database
    my_cursor.close()
    mydb.close()


def deleteShow(movieName, cityName):


    sqldelete = "DELETE FROM movies WHERE movie_name = movieName AND city = cityName "
    
    my_cursor = ''
    mydb = ''
    #establish connection to mysql database and use table movies
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")

    try :
        my_cursor.execute(sqldelete)
        mydb.commit()
        print("Movie Delete Successfully")
    except :
        print("Movies does not exist in the current show list")
    

    my_cursor.close()
    mydb.close()


def createAccount(usertype, email, mobile, password, security_key):

    my_cursor = ''
    mydb = ''

    sqlcreate = ''
    record =(email, mobile, password, security_key)
    
    if usertype == 1:
        sqlcreate = "INSERT INTO admin(email, mobile, password, security_key) VALUES(%s, %s, %s, %s)"
    else :
        sqlcreate = "INSERT INTO user(email, mobile, password, security_key) VALUES(%s, %s, %s, %s)"
    print(sqlcreate)
    #establish connection to mysql database and use table user
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")
    
    try :
        my_cursor.execute(sqlcreate,record)
        mydb.commit()
        status = True
        print("Accound Created Successful")
    except :
        print("Failed to add new user")

    my_cursor.close()
    mydb.close()


# verify user credentials
def login(email, password, usertype):


    my_cursor = ''
    mydb = ''
    usercount = 0

    email = '"' + email + '"'
    password = '"' + password + '"'

    if usertype == 1:

        sqlsearch = "SELECT * FROM admin WHERE email = " + email + " AND " + " password = " + password 

    else :
        
        sqlsearch = "SELECT * FROM user WHERE email = " + email + " AND " + " password = " + password



    #establish connection to mysql database and use table users
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")
    
    try :
        my_cursor.execute(sqlsearch)
        usercount = my_cursor.fetchall()
        print("Login Successful")

    except :
        print("Failed to login")

    my_cursor.close()
    mydb.close()

    if len(usercount) :
            return True
    else:
            return False


# permanent user accound delete
def deleteAccount(email, password):

    my_cursor = ''
    mydb = ''


    email = '"' + email +'"'
    password = '"' + password +'"'

    #sql query for accoundt deletion
    sqlaccounddelete ='"' + "DELETE FROM users WHERE email = " + email +  " AND "  + " password = " + password + '"'

    #establish connection to mysql database and use table movies
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")
    
    # deleting user accound
    try :

        my_cursor.execute(sqlaccounddelete)
        mydb.commit()
        print("Your account has been deleted permanently")

    except :
        print("Account does not exist/ failed")

    #closing connection from database
    my_cursor.close()
    mydb.close()


def changeAccountPassword(email, newpassword):
    
    my_cursor = ''
    mydb = ''


    newpassword = '"' + newpassword + '"'
    email = '"' + email + '"'

    # sql query to update the password
    sqlupdate ='"' + "UPDATE user SET password = " + newpassword + "WHERE email = " + email
    
    # establish database connectivity

    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")

    #updating the password
    try :
        my_cursor.execute(sqlupdate)
        mydb.commit()
        print("password changed successful")
    except :
        print("Failed to change password")
    
    #closing connection from database
    my_cursor.close()
    mydb.close()




#list the available show
def displayShow():

    my_cursor = ''
    mydb = ''


    # establish database connectivity
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")

    try :   
        my_cursor.execute("SELECT * FROM movies")
        result = my_cursor.fetchall()
        print("movie\tcity\t\t\ttime\tavailable_seat")
        print("----\t-----\t\t\t---\t---")
        for row in result:
            print(row[0] + "\t%s" %row[1] + "\t\t%s" %row[2] + "\t%s" %row[3])
    except :
        print("failed to load the shows")

    #closing connection from database
    my_cursor.close()
    mydb.close()


# for displaying personal bookings
def displayMyBooking():

    my_cursor = ''
    mydb = ''
    # establish database connectivity
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")


    # loading personal booked show
    try :   
        my_cursor.execute("SELECT * FROM mybooking")
        result = my_cursor.fetchall()
        print("movie\tcity\t\t\ttime\tbooked_seat")
        print("----\t-----\t\t\t---\t---")
        for row in result:
            print(row[1] + "\t%s" %row[2] + "\t\t%s" %row[3] + "\t%s" %row[4])
    except :
        print("failed to load the shows")

    my_cursor.close()
    mydb.close()

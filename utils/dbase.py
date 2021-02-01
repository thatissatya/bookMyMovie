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
       print("database already exist")


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
        my_cursor.execute("CREATE TABLE movies(movie_name VARCHAR(30),city VARCHAR(20), show_time VARCHAR(8), expire_date VARCHAR(10), available_seat varchar(3))")
       
    except :
        print('show table already exist')

    #table for specific user booked show
    try :
        my_cursor.execute("CREATE TABLE mybooking(email VARCHAR(50), movie_name VARCHAR(30), city VARCHAR(20), show_time VARCHAR(8), totalseat VARCHAR(3))")

    except:
        print("myshow table already exist ")
    
    my_cursor.close()
    mydb.close()
        

#for user account creation
def createAccount(usertype, email, mobile, password, security_key):

    my_cursor = ''
    mydb = ''

    sqlcreate = ''
    record =(email, mobile, password, security_key)
    
    if usertype == 1:
        sqlcreate = "INSERT INTO admin(email, mobile, password, security_key) VALUES(%s, %s, %s, %s)"
    else :
        sqlcreate = "INSERT INTO user(email, mobile, password, security_key) VALUES(%s, %s, %s, %s)"
    
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
    except :
        print("Failed to login")

    my_cursor.close()
    mydb.close()

    if len(usercount) :
            return True
    else:
            return False


# permanent user accound delete
def deleteAccount(usertype, email, password):

    my_cursor = ''
    mydb = ''


    email = '"' + email +'"'
    password = '"' + password +'"'

    #sql query for accoundt deletion
    if usertype == 1:
        sqlaccounddelete = "DELETE FROM admin WHERE email = " + email +  " AND "  + " password = " + password 
    else :
        sqlaccounddelete = "DELETE FROM user WHERE email = " + email +  " AND "  + " password = " + password 

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


# find your password using security key
def showMyPassword(usertype, email, resetKey):

    my_cursor = ''
    mydb = ''

    # sql query to update the password
    if usertype == 1:
        sqlchangepassword = "SELECT *FROM admin WHERE email = %s AND security_key = %s"
    else :
        sqlchangepassword = "SELECT *FROM user WHERE email = %s AND security_key = %s"
    
    record = (email, resetKey)
    # establish database connectivity

    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")

    #updating the password
    try :
        my_cursor.execute(sqlchangepassword, record)
        result = my_cursor.fetchall()
        if len(result):
            print("your password : ", result[0][2])
        else:
            print("email / resetkey wrong, try again")
    except :
        print("cann't find account")
    
    #closing connection from database
    my_cursor.close()
    mydb.close()

def changeAccountPassword(usertype, email, newpassword):
    
    my_cursor = ''
    mydb = ''


    newpassword = '"' + newpassword + '" '
    email = '"' + email + '"'
    

    # sql query to update the password
    if usertype == 1:
        sqlchangepassword = "UPDATE admin SET password = " + newpassword + "WHERE email = " + email 
    else :
        sqlchangepassword =  "UPDATE user SET password = " + newpassword + "WHERE email = " + email 
    
    # establish database connectivity
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")

    #updating the password
    try :
        my_cursor.execute(sqlchangepassword)
        mydb.commit()
        print("password changed successful")
    except :
        print("Failed to change password")
    
    #closing connection from database
    my_cursor.close()
    mydb.close()


# add new show to the list of movies
def createShow(moviename, city, showtime, expiredate, availableseat):
    
    my_cursor = ''
    mydb = ''

    record = (moviename, city, showtime, expiredate, availableseat)

    sqlinsert = "INSERT INTO movies(movie_name, city, show_time, expire_date, available_seat) VALUES(%s, %s, %s, %s, %s)"
    #establish connection to mysql database and use table movies
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")
    
    try :
        my_cursor.execute(sqlinsert, record)
        mydb.commit()
        print("New Show Created Successful")
    except :
        print("Failed to add new show")

    my_cursor.close()
    mydb.close()


#update old shows
def updateShow(moviename, showtime, expiredate):

    my_cursor = ''
    mydb = ''

    showtime = '"' + showtime + '"'

    expiredate = '"' + expiredate + '" '
    moviename = '"' + moviename + '"'

    # sql query to update the password
    sqlupdate = "UPDATE movies SET show_time = " + showtime +", " + " expire_date = "+ expiredate + " WHERE movie_name = " + moviename
    
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


#deleting a show
def deleteShow(movieName, cityName):


    sqldelete = "DELETE FROM movies WHERE movie_name = %s AND city = %s "
    record = (movieName, cityName)
    
    my_cursor = ''
    mydb = ''
    #establish connection to mysql database and use table movies
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")

    try :
        my_cursor.execute(sqldelete, record)
        mydb.commit()
        print("Movie Delete Successfully")
    except :
        print("Movies does not exist in the current show list")
    

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
        print("\t\tmovie\t\tcity\t\ttime\t\texpire_date\tavailable Seat")
        print("")
        for row in result:
            print("%20s       " %row[0] + "%10s    " %row[1] + "   %10s      " %row[2] + "   %10s    " %row[3] + "   %10s    "%row[4])
    except :
        print("failed to load the shows")

    #closing connection from database
    my_cursor.close()
    mydb.close()

#book my show
def bookshow(email, moviename, showtime, city, seat):
    my_cursor = ''
    mydb = ''
    
    record =(email, moviename, city, showtime, seat)
    sqlbookshow = "INSERT INTO mybooking(email, movie_name, city, show_time, totalseat) VALUES(%s, %s, %s, %s, %s)"
    
    # establish database connectivity
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")


    # loading personal booked show
    try :   
        my_cursor.execute(sqlbookshow, record)
        mydb.commit()
        print("show booked successfully")
    except :
        print("Error! could book the show.")

    my_cursor.close()
    mydb.close()


# for displaying personal bookings
def displayMyBooking(email):

    my_cursor = ''
    mydb = ''
    email = '"' + email + '"'
    sqlsearch = "SELECT * FROM mybooking WHERE email = " + email
    # establish database connectivity
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")


    # loading personal booked show
    try :   
        my_cursor.execute(sqlsearch)
        result = my_cursor.fetchall()
        print("\t\tmovie\t\tcity\t\ttime\t\tbooked_seat")
        print("")
        if len(result):
            for row in result:
                print("%20s       " %row[1] + "%10s    " %row[2] + "   %10s      " %row[3] + "   %10s    " %row[4])
        else :
            print("No booking yet")
    except :
        print("failed to load the shows")

    my_cursor.close()
    mydb.close()


#cancel my show
def cancelShow(email, moviename, showtime, city):
    
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cslot = current_time.split(':')
    mslot = showtime.split(':')
    minutes = int(mslot[1]) - int(cslot[1])
    timestamp = (int(mslot[0]) - int(cslot[0]) ) * 60 + minutes
    
    if timestamp < 120:
        print("Cann't be deleted, time difference should be 2hr min")
    else :
    
        my_cursor = ''
        mydb = ''

        record = (email, moviename, showtime, city)

        #query for fetching the record
        sqlsearch = "SELECT *FROM mybooking WHERE email = %s AND movie_name = %s AND show_time = %s AND city = %s"

        #query for deleting the recording
        sqldelete = "DELETE FROM mybooking WHERE email = %s AND movie_name = %s AND show_time = %s AND city = %s"

        # establish database connectivity
        try :
            mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
            my_cursor = mydb.cursor()

        except :
            print("Database doesnot exist")


        # loading personal booked show
        try :   
            my_cursor.execute(sqlsearch, record)
            result = my_cursor.fetchall()
            if len(result):
                my_cursor.execute(sqldelete, record)
                mydb.commit()
                print("Show Deleted")
            else:
                print("No show found ")
        except :
            print("Error! could book the show.")

        my_cursor.close()
        mydb.close()


#update  Seat before and after booking
def seatUpdate(movie, city, time, seat):

    my_cursor = ''
    mydb = ''

    if int(seat) > 10 and int(seat) < -10 :
        print("You can book only max of 10 seat in  a row")
    else:
        
        movie = '"' + movie + '"'
        city  = '"' + city  + '"'
        time = '"'  + time + '"'

        sqlfetch = "SELECT * FROM  movies WHERE movie_name = " + movie + " AND city = " + city + " AND show_time = " + time
        #print(sqlfetch)

        try :
            mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
            my_cursor = mydb.cursor()

        except :
            print("Database doesnot exist")

        try :   
            my_cursor.execute(sqlfetch)
            result = my_cursor.fetchall()
            avail_seat = int(result[0][4])
            if( int(seat) > avail_seat):
                print(seat, " Seat is not available ")
            else:

               remain_seat = avail_seat - int(seat) 
               remain_seat = '"' + str(remain_seat) +'"'
               sqlupdate = "UPDATE movies SET available_seat = " + remain_seat + " WHERE movie_name = " + movie + " AND city = " + city + " AND show_time = " + time
               #print(sqlupdate)
               my_cursor.execute(sqlupdate)
               mydb.commit()
               print("ticket booked successful")


        except :
            print("failed to fetch data/ update tables")

        #closing connection from database
        my_cursor.close()
        mydb.close()


# get total no. of seat booked
def getSeatCount(email, movie, city, showtime):

    my_cursor = ''
    mydb = ''
    avail_seat = 0

    
    movie = '"' + movie + '"'
    city  = '"' + city  + '"'
    showtime = '"'  + showtime + '"'
    email = '"' + email + '"'

    sqlfetch = "SELECT * FROM  mybooking WHERE movie_name = " + movie + " AND city = " + city + " AND show_time = " + showtime + " AND email = " + email
    #print(sqlfetch)

    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")

    try :   
        my_cursor.execute(sqlfetch)
        result = my_cursor.fetchall()
        
        if len(result) :
            avail_seat = int(result[0][4])
        else:
            avail_seat = 0
        

    except :
        print("failed to fetch data/ update tables")

    #closing connection from database
    my_cursor.close()
    mydb.close()

    return avail_seat

#search by city
def searchByCity(city):

    my_cursor = ''
    mydb = ''
    city = '"' + city + '"'
    sqlfetch = "SELECT * FROM movies WHERE city = " + city
    # establish database connectivity
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")

    try :   
        my_cursor.execute(sqlfetch)
        result = my_cursor.fetchall()
        print("\t\tmovie\t\tcity\t\ttime\t\texpire_date\tavailable Seat")
        print("")
        for row in result:
            print("%20s       " %row[0] + "%10s    " %row[1] + "   %10s      " %row[2] + "   %10s    " %row[3] + "   %10s    "%row[4])

    except :
        print("failed to fetch data")

    #closing connection from database
    my_cursor.close()
    mydb.close()


#search by  time
def searchByTime(showtime):

    my_cursor = ''
    mydb = ''

    showtime = '"' + showtime + '"'
    sqlfetch = "SELECT * FROM movies WHERE city = " + showtime
    # establish database connectivity
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")

    try :   
        my_cursor.execute(sqlfetch)
        result = my_cursor.fetchall()
        print("\t\tmovie\t\tcity\t\ttime\t\texpire_date\tavailable Seat")
        print("")
        for row in result:
            print("%20s       " %row[0] + "%10s    " %row[1] + "   %10s      " %row[2] + "   %10s    " %row[3] + "   %10s    "%row[4])

    except :
        print("failed to verify redundancy")

    #closing connection from database
    my_cursor.close()
    mydb.close()


#search by movie name
def searchByName(moviename):

    my_cursor = ''
    mydb = ''
    moviename = '"' + moviename + '"'
    sqlfetch = "SELECT *FROM movies WHERE movie_name = " + moviename
    # establish database connectivity
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")

    try :   
        my_cursor.execute(sqlfetch)
        result = my_cursor.fetchall()
        print("\t\tmovie\t\tcity\t\ttime\t\texpire_date\tavailable Seat")
        print("")
        for row in result:
            print("%20s       " %row[0] + "%10s    " %row[1] + "   %10s      " %row[2] + "   %10s    " %row[3] + "   %10s    "%row[4])
    except :
        print("failed to verify redundancy")

    #closing connection from database
    my_cursor.close()
    mydb.close()


#check whether show exist or not
def checkDuplicate(moviename, showtime, city):

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
        for row in result:
            if row[0] == moviename and row[1] == city and row[2] == showtime:
                return False
            
    except :
        print("failed to verify redundancy")

    #closing connection from database
    my_cursor.close()
    mydb.close()
    return True
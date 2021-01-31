import mysql.connector

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
        print(usercount)
        if len(usercount) :
            print("Login Successful")
    except :
        print("Failed to login")

    my_cursor.close()
    mydb.close()

    



login("prakash@nitt.edu","12345", 2)
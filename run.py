import mysql.connector

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

showMyPassword(1, "satya@nitt.edu", "1254") 
import mysql.connector

def cancelShow(email, moviename, city, showtime):
    
    from datetime import datetime
    now = datetime.now()
    flag = False
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
            print("Show Deleted")
        else:
            print("Delete show before 2hr / booking not found")
    except :
        print("Error! could book the show.")

    my_cursor.close()
    mydb.close()

cancelShow('satya@nitt.edu','bloodshot', 'indore' ,'08:30:00') 
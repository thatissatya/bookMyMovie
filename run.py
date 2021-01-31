import mysql.connector

def bookshow(email, moviename, showtime, city, seat):
    my_cursor = ''
    mydb = ''

    record =(email, moviename, showtime, city, seat)
    sqlbookshow = "INSERT INTO mybooking(email, movie_name, city, show_time, totalseat ) VALUES(%s, %s, %s, %s, %s)"
    # establish database connectivity
    try :
        mydb = mysql.connector.connect(host = 'localhost', user ='satya', passwd ='admin', database = 'bookmymovie')
        my_cursor = mydb.cursor()

    except :
        print("Database doesnot exist")


    # loading personal booked show
    try :   
        my_cursor.execute(sqlbookshow, record)

        print("show booked successfully")
    except :
        print("Error! could book the show.")

    my_cursor.close()
    mydb.close()



bookshow("satya@nitt.edu", "avatar","indore", "6:20:00", 10)
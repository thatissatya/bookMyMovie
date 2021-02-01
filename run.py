import mysql.connector

def getSeatCount(email, movie, city, showtime):

    my_cursor = ''
    mydb = ''
    avail_seat = 0

    
    movie = '"' + movie + '"'
    city  = '"' + city  + '"'
    showtime = '"'  + showtime + '"'
    email = '"' + email + '"'

    sqlfetch = "SELECT * FROM  mybooking WHERE movie_name = " + movie + " AND city = " + city + " AND show_time = " + showtime + " AND email = " + email
    print(sqlfetch)

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


print(getSeatCount('satya@nitt.edu', 'bloodshot', 'indore', '08:30:00'))
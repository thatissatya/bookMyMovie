import mysql.connector

mydb = mysql.connector.connect(host ='localhost', user = 'root', passwd = 'toor', database = 'nitt')


my_cursor = mydb.cursor()



try :
    my_cursor.execute("CREATE TABLE trex(day  varchar(10), ts varchar(8))")
except :
    print("table already exist")
d = "'1996-01-22'"
t = "08:00:00"
#sqlinsert = "INSERT INTO trex(day, ts) VALUES(%s, %s)"
record = (d)
# my_cursor.execute(sqlinsert, record)
# mydb.commit()


# record = ("1996-01-22")
sqldel = "DELETE FROM trex WHERE day = " + d
print(sqldel)
my_cursor.execute(sqldel)
mydb.commit()
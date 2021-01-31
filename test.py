import random
print(random.randint(1000,10000))

import mysql.connector

mydb = mysql.connector.connect(host ='localhost', user = 'root', passwd = 'toor', database = 'nitt')
mycr = mydb.cursor()
print(mycr)
# var = mycr.execute("CREATE DATABASE nitt")
# mycr.close()
# mydb.close()
my_cursor = mydb.cursor()

#table for admin credentials
my_cursor.execute("CREATE TABLE admin(email VARCHAR(50) PRIMARY KEY, mobile BIGINT(10), password VARCHAR(10), security_key INT(4))")





import mysql.connector

#SET MYSQL CONNECTION
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "password123",
	database = "testdb",
	)

#CREATE CURSOR INSTANCE
my_cursor = mydb.cursor()

#CREATE DATABASE
my_cursor.execute("CREATE DATABASE testdb")

#SHOW DATABASE
my_cursor.execute("SHOW DATABASES")

#CREATE TABLE
my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
my_cursor.execute("SHOW TABLES")

#INSERT ONE RECORD
sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
record1 = ("John", "john@codemy.com", 40)
my_cursor.execute(sqlStuff, record1)
mydb.commit()

#INSERT MULTIPLE RECORDS
sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
records = [("Tim", "tim@tim.com", 32),
	("Mary", "Mary@mary.com", 21),
	("Steve", "steve@steveEmail.com", 57),
	("Tina", "tina@somethingellse.com", 29),]
my_cursor.executemany(sqlStuff, records)
mydb.commit()

#PULL DATA FROM THE TABLE
my_cursor.execute("SELECT * FROM users")
result = my_cursor.fetchall()
print("NAME\tEMAIL\t\t\tAGE\tID")
print("----\t-----\t\t\t---\t---")
for row in result:
	print(row[0] + "\t%s" %row[1] + "\t\t%s" %row[2] + "\t%s" %row[3])

#WHERE CLAUSE
my_cursor.execute("SELECT * FROM users WHERE name =  'John'")
result = my_cursor.fetchall()
for row in result:
	print(row)

#WHERE and LIKE WILDCARDS
my_cursor.execute("SELECT * FROM users WHERE name LIKE '%i%'")
result = my_cursor.fetchall()
for row in result:
	print(row)

# AND / OR Clause
my_cursor.execute("SELECT * FROM users WHERE name LIKE '%i%' AND age = 29 AND user_id = 5")
result = my_cursor.fetchall()
for row in result:
	print(row)

#UPDATING RECORDS
my_sql = "UPDATE users SET name = 'Johnny' WHERE user_id = 6"
my_cursor.execute(my_sql)
mydb.commit()

#LIMIT RESULTS
my_cursor.execute("SELECT * FROM users LIMIT 3 OFFSET 1")
result = my_cursor.fetchall()
for row in result:
	print(row)

#ORDERING RESULTS
my_cursor.execute("SELECT * FROM users ORDER BY age DESC")
result = my_cursor.fetchall()
for row in result:
	print(row)

#DELETE RECORDS
my_sql = "DELETE FROM users WHERE name  = 'John'"
my_cursor.execute(my_sql)
mydb.commit()

# DELETE DROP TABLE
my_sql = "DROP TABLE IF EXISTS users"
my_cursor.execute(my_sql)


# import mysql.connector 

# # mydb = mysql.connector.connect(host ='localhost', user = 'root' , passwd = 'toor',  auth_plugin='mysql_native_password')

# # my_cur = mydb.cursor()

# # #var = my_cur.execute('create database satya') # for creation of database

# # # my_cur.execute('show databases') #show existing databases

# # for db in my_cur:
# #     print(db[0])

# mydb = mysql.connector.connect(host ='localhost', user = 'root' ,
#  passwd = 'toor', 
#  database = 'satya'
#  )

# my_cursor = mydb.cursor()

# #my_cursor.execute("CREATE TABLE person (name varchar(25) UNIQUE, city varchar(50))")
# # my_cursor.execute("SHOW TABLES")

# # for table in my_cursor:
# #     print(table[0])
# # sqlinsert = "INSERT INTO person(name, city) VALUES(%s, %s)"
# # record =("SATYA", "INDORE")
# # my_cursor.execute("INSERT INTO person(%s, %s) VALUES("anshu", "bihar")")
# # mydb.commit()
# my_cursor.execute("UPDATE person SET city = 'gopalganj' where city = 'INDORE' ")
# my_cursor.execute("select *from person where city = 'gopalganj'")
# result = my_cursor.fetchall()

# for row in result:
#     print(row)
#     print(type(row))
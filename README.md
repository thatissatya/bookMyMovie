# bookMyMovie
Python + Backend (CLI based movie booking System)

<!-- 1. Write a Python Console application for the movie booking system with any database whichever you are comfortable as backend. Here are the options that we would like to have in this application:  
    a. list all the movie shows available with movie name, timings
    b. Check for the availability of the movie shows based on the name or date
    c. Book a movie for any number of seats that you want to book up to 10 in a single transaction
    d. Cancel the movie before 2 hours of the show time
    e. Manage movies (add, delete, update movie/show details)   

Note: Create database schema, necessary tables and initial data as per the need to achieve the same
Reference: https://in.bookmyshow.com -->

 table details : admin - admin(email,mobile,password, securityKey)
 table details : user - user(email,mobile,password, securityKey)
 table details : movies - movies(movie_name VARCHAR(30),city VARCHAR(20), show_time VARCHAR(8), expire_date VARCHAR(10), available_seat varchar(3))
 table details :mybooking - mybooking(email VARCHAR(50), movie_name VARCHAR(30), city VARCHAR(20), show_time VARCHAR(8), totalseat INT)
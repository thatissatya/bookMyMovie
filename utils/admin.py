from os import system
from utils.dbase import createShow
from utils.dbase import displayShow
from utils.dbase import deleteShow
from utils.dbase import updateShow
from utils.dbase import changeAccountPassword
from utils.dbase import checkDuplicate


def adminPanel(usertype, email):

    #admin work --- admin panel
    while True:

        #admin can either add a new show or remove and existing show
        choice = int(input("1. Add Show\n2. Remove Show\n3. Update Show\n4. View Availabe Show\n5. Change Password\n6. Logout : "))

        if choice == 1:

            movieName = input("Enter Movie Name : ")
            city = input("Enter City Name : ")
            showtimes = input("Enter Slot time(HH:MM:SS) : ")
            expiredate = input("Enter last day(YYYY-MM-DD) of the show : ")
            seatAvailable = input("Enter No. of Seats : ")
            if checkDuplicate(movieName, showtimes, city):
                createShow(movieName,city, showtimes, expiredate, seatAvailable)
            else:
                print("The show already exists ...")

        elif choice == 2:

            movieName = input("Enter Movie Name : ")
            city = input("Enter city Name : ")
            deleteShow(movieName, city)

        elif choice == 3:
            movieName = input("Enter Movie Name : ")
            showtime = input("Enter New Slot Time(HH:MM:SS) Name : ")
            expiredate = input("Enter New expire date (YYYY-MM-DD) of movie : ")
            updateShow(movieName, showtime, expiredate)

        elif choice == 4:
            displayShow()

        elif choice == 5:
            newpassword = input("Enter New Password : ")
            changeAccountPassword(usertype, email, newpassword)

        elif choice == 6:
            break

        else:
            print("wrong input, Try Again ")

        


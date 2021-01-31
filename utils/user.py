from os import system
from utils.dbase import displayMyBooking, displayShow
from utils.dbase import bookshow
from utils.dbase import bookshow
from utils.dbase import cancelShow
from utils.dbase import searchByCity, searchByName, searchByTime
from utils.dbase import changeAccountPassword

def userPanel(usertype, email):

    #user work --- user panel
    while True:

        #admin can either add a new show or remove and existing show
        choice = int(input("1. Display Show\n2. Book Show\n3. My Bookings\n4. Cancel Show\n5. Filter Movie\n6. Change Password\n7. Logout : "))

        if choice == 1:
            displayShow()

        elif choice == 2:

            movieName = input("Enter Movie Name : ")
            showtime = input("Enter New Slot time(HH:MM:SS) : ")
            city = input("Enter city Name : ")
            totalseat = input("Enter No. of seat : ")
            bookshow(email, movieName, showtime, city, totalseat)

        elif choice == 3:
            
            displayMyBooking(email)

        elif choice == 4:
            movieName = input("Enter Movie Name : ")
            showtime = input("Enter New showtime(HH:MM:SS) Name : ")
            city = input("Enter city Name : ")
            cancelShow(email, movieName, showtime, city)

        elif choice == 5:
            choice = int(input("press:\n1. Search by City\n2. Search by Name\n3. Search by Time : "))
            
            if choice == 1:
                city = input("Enter city Name : ")
                searchByCity(city)
            elif choice == 2:
                moviename = input("Enter the Movie Name : ")
                searchByName(moviename)
            elif choice == 3:
                slot = input("Enter Movie Time(HH:MM:SS) : ")
                searchByTime(slot)
            else:
                print("Wrong Choice try again .. ")

        elif choice == 6:

            newpassword = input("Enter new Password : ")
            changeAccountPassword(usertype, email, newpassword)

        elif choice == 7:
            break

        else:
            print("wrong input, Try Again ")

        


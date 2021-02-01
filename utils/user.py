from os import system
from run import getSeatCount
from utils.dbase import displayMyBooking, displayShow
from utils.dbase import bookshow
from utils.dbase import bookshow
from utils.dbase import cancelShow
from utils.dbase import searchByCity, searchByName, searchByTime
from utils.dbase import changeAccountPassword
from utils.dbase import seatUpdate


def userPanel(usertype, email):

    #user work --- user panel
    while True:

        #admin can either add a new show or remove and existing show
        choice = int(input("1. Display Show\n2. Book Show\n3. My Bookings\n4. Cancel Show\n5. Filter Movie\n6. Change Password\n7. Logout : "))
        system('cls')
        if choice == 1:
            displayShow()

        elif choice == 2:

            movieName = input("Enter Movie Name : ")
            showtime = input("Enter New Slot time(HH:MM:SS) : ")
            city = input("Enter city Name : ")
            totalseat = input("Enter No. of seat : ")
            if int(totalseat) >10 or int(totalseat) < 1:
                system('cls')
                print("seat no. must be between 1 - 10")
                continue
            try:
                seatUpdate(movieName, city, showtime, totalseat)
            except: 
                print("could not update the seat ...")
            try:
                bookshow(email, movieName, showtime, city, totalseat)
            except:
                print("could not book show , server error")

        elif choice == 3:
            
            displayMyBooking(email)

        elif choice == 4:
            movieName = input("Enter Movie Name : ")
            showtime = input("Enter New showtime(HH:MM:SS) Name : ")
            city = input("Enter city Name : ")
            totalseat = getSeatCount(email, movieName, city, showtime)
            if(int(totalseat) == 0):
                print("You have no booking for above detailse")
            else:
                seatUpdate(movieName, city, showtime, str(totalseat))
                cancelShow(email, movieName, showtime, city)

        elif choice == 5:

            choice = ''
            try :
             choice = int(input("press:\n1. Search by City\n2. Search by Name\n3. Search by Time : "))
            except:
                print("please Enter integer value : ")
                
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
            system('cls')
            break

        else:
            print("wrong input, Try Again ")

        


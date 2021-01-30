from utils.addShow import addNewShow
from utils.removeShow import dropShow

def adminPanel():

    #admin work --- admin panel
    while True:

        #admin can either add a new show or remove and existing show
        choice = int(input("1. Add Show\n2. Remove Show\n3. Update Show\n4. Logout "))

        if choice == 1:
            movieName = input("Enter Movie Name : ")
            showtimes = input("Enter Show time ")
            seatAvailable = int(input("Enter No. of Seats : "))
            lastdateofShow = input("Enter last day of the show")
            addNewShow(movieName, showtimes, seatAvailable, lastdateofShow)

        elif choice == 2:
            print("removing show ...")
        
        elif choice == 3:
            print("Updating show .. ")

        elif choice == 4:
            break

        else:
            print("wrong input, Try Again ")


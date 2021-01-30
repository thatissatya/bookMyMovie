from utils.addShow import addNewShow
from utils.removeShow import dropShow

def adminPanel():

    #admin work --- admin panel
    while True:

        #admin can either add a new show or remove and existing show
        choice = int(input("1. Add Show\n2. Remove Show\n3. Logout "))

        if choice == 1:
            print("adding show ...")
        elif choice == 2:
            print("removing show ...")
        elif choice == 3:
            break
        else:
            print("wrong input, Try Again ")


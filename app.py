from utils.login import userlogin
from utils.singup import usersignup
from utils.recoverAccount import getYourPassword
from utils.dbase import dbCreate, tableCreate

if __name__ == '__main__':

    try :
        dbCreate()
        tableCreate()
        while True:

            #command line option visible to end-user
            choice = int(input("1. Login \n2. Sign-up\n3. Reset Password\n4. Exit : "))

            if choice == 1:
                email = input("Enter E-mail : ")
                password = input("Enter Password : ")
                usertype = int(input("Enter\n 1. for Admin\n 2. for Customer "))
                userlogin(usertype, email, password)
                

            elif choice == 2:
                email = input("Enter E-mail : ")
                mobile = input("Enter Mobile No. : ")
                password = input("Enter Password : ")
                usertype = int(input("Enter\n 1. for Admin\n 2. for Customer "))
                usersignup(usertype, email, mobile, password)

            elif choice == 3:
                email = input("Enter E-mail : ")
                mobile = input("Enter Mobile No. : ")
                resetkey = input("Enter 4 digit unique resetKey : ")
                print(getYourPassword(email, mobile, resetkey))

            elif choice == 4:
                exit()

            else :
                print("wrong Choice, Try again ...")

    except :
            print("Program closed /Failed to load server")

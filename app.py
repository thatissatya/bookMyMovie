from utils.login import userlogin
from utils.singup import usersignup


if __name__ == '__main__':
    while True:

        #command line option visible to end-user
        choice = int(input("1. login \n2. sign-up\n3. exit"))

        if choice == 1:
            email = input("Enter E-mail : ")
            password = input("Enter Password : ")
            userlogin(email, password)

        elif choice == 2:
            email = input("Enter E-mail : ")
            mobile = input("Enter Mobile No. : ")
            password = input("Enter Password : ")
            usersignup(email, mobile, password)

        elif choice == 3:
            exit()

        else :
            print("wrong Choice, Try again ...")

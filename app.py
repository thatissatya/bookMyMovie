from utils.login import ulogin
from utils.singup import usignup
if __name__ == '__main__':
    while True:
        print("1. login \n2. sign-up\n3. exit ")
        choice = int(input())
        if choice == 1:
            email = input("Enter E-mail : ")
            password = input("Enter Password : ")
            print(email +  password)
        elif choice == 2:
            email = input("Enter E-mail : ")
            mobile = input("Enter Mobile No. : ")
            password = input("Enter Password : ")
            print(mobile)
        elif choice == 3:
            exit()
        else :
            print("wrong Choice, Try again ...")

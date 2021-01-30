from utils.credentialverifier import verifyEmail
from utils.admin import adminPanel
from utils.user import userPanel

def userlogin(email, password):

    #check the validity of the credentials
    if verifyEmail(email):

        fptr = open('users.txt', 'r')
        usercredential = fptr.readlines()
        usercredential = usercredential[0].split()
        fptr.close()
        #verifying the existing user

        flag = False

        for user in usercredential:
            details = user.split('-')
            if email == details[0] and password == details[2]  :
                flag = True
                print("Login Successfull")
                break

        # if user is admin, jump to adminPanel or switch to userPanel
        if flag :
            if email == 'satya@gamil.com':
                    adminPanel()
            else :
                    userPanel()

        else :
            print("user not found")
    else :
        print("invalid email, try again ")

from utils.credentialverifier import verifyEmail
from utils.admin import adminPanel
from utils.user import userPanel
from utils.dbase import login


def userlogin(usertype, email, password):

    #check the validity of the credentials
    if verifyEmail(email):
        if usertype == 1:

            if login(email, password, usertype) :
                print("Login Successful")
                adminPanel(usertype, email)
            else:
                print("Username / Password did not match, try again ...")
                
                
        elif usertype == 2:

            if login(email, password, usertype):
                print("Login Successful")
                userPanel(usertype, email)
            else:
                print("Username / Password did not match, try again ...")

        else :

                print("Wrong Usertype. Try Again")
       
        
    else :
        print("invalid email, try again ")
         

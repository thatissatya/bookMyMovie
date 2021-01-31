from utils.credentialverifier import verifyEmail
from utils.dbase import showMyPassword

#reset the password of user in case he forgets
def getYourPassword(usertype, email, security_ques):

    #validate the email and password
    if verifyEmail(email):

        showMyPassword(usertype,email, security_ques)
        
    else:
        print("invalid email address")


            

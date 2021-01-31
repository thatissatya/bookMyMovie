import random
from utils.credentialverifier import verifyMobile, verifyEmail
from utils.dbase import createAccount

def usersignup(usertype, email, mobile, password):

    #security Key generation
    resetKey = random.randint(1000,10000)

    #before user creation verify the email and mobile no.
    if verifyEmail(email) and  verifyMobile(mobile) :

        createAccount(usertype , email, mobile, password, resetKey)

    else :
        print("Error, input not valid ")
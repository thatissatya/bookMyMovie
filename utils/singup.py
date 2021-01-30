import random
from utils.credentialverifier import verifyMobile, verifyEmail


def usersignup(email, mobile, password):
    resetKey = random.randint(1000,10000)
    #before user creation verify the email and mobile no.
    if verifyEmail(email) and  verifyMobile(mobile) :
        
        fptr = open('users.txt','a')
        user = email + '-' + str(mobile) + '-' + password + "-" + str(resetKey) + ' '
        fptr.write(user)
        fptr.close()
        print("Note down the password reset key : ", resetKey)
        print("Successfully Registered ")

    else :
        print("Error, input not valid ")
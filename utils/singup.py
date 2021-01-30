from utils.credentialverifier import verifyMobile, verifyEmail


def usersignup(email, mobile, password):
    
    #before user creation verify the email and mobile no.
    if verifyEmail(email) and  verifyMobile(mobile) :
        
        fptr = open('users.txt','a')
        user = email + '-' + str(mobile) + '-' + password + " "
        fptr.write(user)
        fptr.close()

        print("Successfully Registered ")

    else :
        print("Error, input not valid ")
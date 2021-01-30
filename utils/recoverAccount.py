from utils.credentialverifier import verifyEmail, verifyMobile


#reset the password of user in case he forgets
def getYourPassword(email, mobile, security_ques):

    #validate the email and password
    if verifyEmail(email) and verifyMobile(mobile):

        fptr = open('users.txt', 'r')
        usercredential = fptr.readlines()
        usercredential = usercredential[0].split()
        fptr.close()
        #verifying the existing user details

        flag = False

        for user in usercredential:
            details = user.split('-')

            #if user details found
            if email == details[0] and mobile == details[1] and security_ques == details[3] :
                return details[2]

        return "user not found, check your email/mobile/resetKey "   

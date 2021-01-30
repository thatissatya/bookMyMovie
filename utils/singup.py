from utils.credentialverifier import verifyMobile, verifyEmail


def usignup(email, mobile, password):

    if verifyEmail(email) and  verifyMobile(mobile) :
        print("Sign Up")
        
    print("Successfully Registered ")
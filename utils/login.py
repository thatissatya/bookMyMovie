from utils.credentialverifier import verifyEmail

def ulogin(email, password):
    if verifyEmail(email):
        print("trying login")
    print("Loging Successful")
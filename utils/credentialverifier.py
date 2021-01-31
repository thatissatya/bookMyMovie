from re import search

# email verification
def verifyEmail(email):

    pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if search(pattern, email) :
        return True
    else :
        return False

#verify mobile no.
def verifyMobile(mobile):

    if len(mobile) < 10 or len(mobile) > 10 and mobile[0] < 6:
        return False
    else :
        return True
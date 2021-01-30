# ensure the integrity and consistency of the shows and users

#check whether show already exist in show list or not
def movieNameCheck(movie):
    show = ''

    try :
        fptr = open('showlist.txt', 'r')
        show = fptr.readlines()
        fptr.close()
    except :
        print("Error! unable to access database ")

    show = show.split()
    movies = [each.split('-')[0] for each in show]

    if movie in movies:
        return False

    return True


#check whether the email is already registered or not
def userCheck(email):
    userlist = ''

    try :
        fptr = open('users.txt', 'r')
        userlist = fptr.readlines()
        fptr.close()
    except :
        print("Error! unable to access database ")

    userlist = userlist.split()
    emails = [each.split('-')[0] for each in userlist]

    if email in emails:
        return False

    return True


#check whether the mobile no. is already available int he database or not
def mobileCheck(mobile):
    userlist = ''

    try :
        fptr = open('users.txt', 'r')
        userlist = fptr.readlines()
        fptr.close()
    except :
        print("Error! unable to access database ")

    userlist = userlist.split()
    mobileNos = [each.split('-')[1] for each in userlist]

    if mobile in mobileNos:
        return False

    return True
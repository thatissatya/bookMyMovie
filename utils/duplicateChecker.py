

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

def userCheck(email):
    userlist = ''

    try :
        fptr = open('users.txt', 'r')
        userlist = fptr.readlines()
        fptr.close()
    except :
        print("Error! unable to access database ")

    user = userlist.split()
    emails = [each.split('-')[0] for each in userlist]

    if email in emails:
        return False

    return True
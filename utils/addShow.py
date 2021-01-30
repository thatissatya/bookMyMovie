from utils.duplicateChecker import movieNameCheck


def addNewShow(movie, showtimes, seats, lastdateofshow):

    if movieNameCheck(movie) :
        # verify for user access permission
        try :
            fptr = open('showlist.txt', 'a')
            show = movie +  '-' + showtimes + '-' + str(seats) + '-' + lastdateofshow + ' '
            fptr.write(show)
            fptr.close()

        except :
            return "Error ! failed to add show, Database Error"

        return "Show added Successfully"

    else :
        return "This movie already Exist in show, try to update the show... "

def displayAvailableShow():

    showlist = ''
    try :

        fptr = open('showlist.txt', 'r')
        showlist = fptr.readlines()
        fptr.close()

    except :
        print("Error! Database access failed ...")
    
    showlist = showlist.split()

    sno = 0
    print('S.no ' +'  '  + 'Movie Name ' + '  ' 'Time ' +'  '  + 'Availabe Seats ' + '  '  )
    for shows in showlist :

        details = shows.split('-')
        showname  = str(sno)  +'   '  + details[0] + '  ' + details[1] + details[2]
        print(showname)



def cornfieldpoopinasock():
    wrongvar = input ("You deside to enter the corn maze, would you like to continue? or go back to the farm.")
    if wrongvar == ("continue"):
        input ("You decide to continue into the maze. ")
        leftorright1stplaceloser()

    elif wrongvar == ("go back"):
        input ("You decide to head back. ")
        #Once this merges back with farmhub we will load that
    else:
        print ("I am sorry I do not understand, please use english. ")
    cornfieldpoopinasock()





def leftorright1stplaceloser():
    leftorright1stplaceloser = input("you continue into the maze would you like to go left right or back to the start").strip().lower()

    if  leftorright1stplaceloser == ("left"):
        input ("You deside to go left")
        firstplaceleftforwardorrighthampickle()
    elif leftorright1stplaceloser == ("right"):
        input ("You deside to go right")
        rightpathbananacreampineapple()
    else:
        print ("I am sorry I do not understand why you can not type")
    
    leftorright1stplaceloser()
leftorright1stplaceloser()



def firstplaceleftforwardorrighthampickle():
    fungijim = input ("You deside to continue into the maze, would you like to go forwards, the path to the right, or back to the last decition")

    if fungijim == ("forward"):
        input ("You continue heading forward")
        winorloseorbacksideleftgalafray()
    elif fungijim == ("right"):
        input ("You deside to head down the right path.")

    elif fungijim == ("go back"):
        input ("You head back to your last decition")

    else:
        print ("I am sorry please type")
    firstplaceleftforwardorrighthampickle()
firstplaceleftforwardorrighthampickle()



def deadendrubberwall():
    flubberblubber = input ("oh no ran into a dead end. would you like to go back to last intersection, or back to the start?")

    if flubberblubber == ("go back"):
        input ("You  deside to head back to the last section")

    elif flubberblubber == ("beginning"):
        input ("you head back the way you came")

    else:
        print ("this here is a failior to co mu no cate")
    deadendrubberwall()
deadendrubberwall()



def winorloseorbacksideleftgalafray():
    brusewayne = input("you continue into the maze, would you like to go left, right, or go back to the last decition.")

    if brusewayne == ("left"):
        input ("You deside to turn left")

    elif brusewayne == ("right"):
        input ("You deside to go right")

    elif brusewayne == ("go back"):
        input ("You head back to the last decition")

    else:
        ("please restate your answer, but this time in english")
    winorloseorbacksideleftgalafray()
winorloseorbacksideleftgalafray()



def rightpathbananacreampineapple():
    bucketoflubber = input ("You continue into the maze, wood you like to go forward, right, or back to the last intersetion")

    if bucketoflubber == ("forward"):
        input ("You continue forward")

    elif bucketoflubber == ("right"):
        input ("you deside to go to the right")

    elif bucketoflubber == ("go back"):
        input ("you deside to go back")

    else:
        ("invalid syntex typing error")
    rightpathbananacreampineapple() 
rightpathbananacreampineapple()

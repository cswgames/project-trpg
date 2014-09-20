def runeofthechubaca():
    input ("you are in mysterius temple. ")

    bobthecan = input ("there are 2 paths, would you like to go left or right. ")

    if bobthecan == ("left"):
        input ("you decide to head to the left. ")
        rune1leftfunnydog()
    elif bobthecan == ("right"):
        input ("you deside to head to the right. ")
        jackhasnoswag()
    else:
        input ("I am sorry I do not understand. ")
    runeofthechubaca()

#decition left when you enter ----------------------------------------------

def rune1leftfunnydog():
    input ("you find a key {1509} to the crypt and you continue walking")
    input ("you find a coradoor to the right side...")
    input ("you find a crate with a lock, look around for a key. ")


    blanketofsnow = input ("you need to find the key to the box would you like to continue or go back, to the door")
    
    if blanketofsnow == ("continue"):
        input ("you head forward in search for the key. ")
        theswarmofbeavers()
#enemy for the area is called "the swarm"
    elif blanketofsnow == ("go back"):
        input ("you go back to see if you can get into the crypt. ")
        rune1leftfunnydog()

#decition to go to the right------------------------------------------------

def jackhasnoswag():
    input ("you reach the crypt door")

    jackneedstoshower = input ("if you know the key code type it in, if not go back. ")

    if jackneedstoshower == ("1509"):
        input ("you enter the crypt")
        cryptofthetaco()

    elif jackneedstoshower == ("go back"):
        input ("you head back to the start to find the key. ")
        runeofthechubaca()

    else:
        input ("I am sorry I do not understand")
        jackhasnoswag()

#crypt function--------------------------------------------------------------

def cryptofthetaco():
    input ("you enter the crypt to find the swarm overlord. ")
#if win ("you find chest key 12667")
#if lose GAMEOVER


#after battle function for blanketofsnow-------------------------------------------------------


def theswarmofbeavers():
    input ("oh no you encounter a swarmberserker! ")
#if win ("you find a LVL. 8")
#if lose GAMEOVER




runeofthechubaca()

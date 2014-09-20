input ("You enter a mysterious temple. ")
def runeofthechubaca():
    bobthecan = input ("There are 2 paths, would you like to go left or right. >").strip().lower()

    if bobthecan == "left":
        input ("You decide to head to the left. ")
        rune1leftfunnydog()
    elif bobthecan == "right":
        input ("You deside to head to the right. ")
        jackhasnoswag()
    else:
        input ("I am sorry I do not understand. ")
    runeofthechubaca()

#decition left when you enter ----------------------------------------------

def rune1leftfunnydog():
    input ("You find a key {1509} to the crypt and you continue walking")
    input ("You find a coradoor to the right side...")
    input ("You find a crate with a lock, look around for a key. ")


    blanketofsnow = input ("You need to find the key to the box would you like to continue or go back, to the door").strip().lower()
    
    if blanketofsnow == "continue":
        input ("you head forward in search for the key. ")
        theswarmofbeavers()
#enemy for the area is called "the swarm"
    elif blanketofsnow == ("go back"):
        input ("you go back to see if you can get into the crypt. ")
        rune1leftfunnydog()

#decition to go to the right------------------------------------------------

def jackhasnoswag():
    input ("you reach the crypt door")

    jackneedstoshower = input ("if you know the key code type it in, if not go back. ").strip().lower()

    if jackneedstoshower == ("1509"):
        input ("The slides You enter the crypt")
        cryptofthetaco()

    elif jackneedstoshower == ("go back"):
        input ("You head back to the start to find the key. ")
        runeofthechubaca()

    else:
        input ("I am sorry I do not understand")
        jackhasnoswag()

#crypt function--------------------------------------------------------------

def cryptofthetaco():
    input ("You enter the crypt to find the swarm overlord. ")
#if win ("you find chest key 12667")
#if lose GAMEOVER


#after battle function for blanketofsnow-------------------------------------------------------


def theswarmofbeavers():
    input ("oh no you encounter a swarmberserker! ")
#if win ("you find a LVL. 8")
#if lose GAMEOVER




runeofthechubaca()

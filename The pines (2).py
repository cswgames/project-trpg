input ("You arise")
input ("you notice the cool, light weight of the thin sheet of fabric covering your body")
input ("darkness")
input ("silence")
input ("you light the candle aside your bed")
input ("and prepare for your day")
input ("You enter The Pines")
def pinehelpfunc():
    if pinehelp == ("i3qr"):
        input("He is saved because of you! here take this LVL 1 Armor, It will help on your quest.")
    else:
        input ("That's no help!")
        pinehelp = input ("What is the code?!")
        pinehelpfunc()
            
def pineforest
    di = input("Tau Castle is infront of you, the deep woods are to your right, The Pines are behind you, and the mountains are to your left")
    if di == ("up"):
        input("You Decide to head onward to Tau Castle")
    elif di == ("right"):
        input("You Decide to head right, into the deep woods")
    elif di == ("left"):
        input("You Decide to head left, into the mountain ranges")
    elif di == ("down"):
        input("You Decide to head back to the Pines")
        pines()

def pines():
    pine = input("There's the Blacksmith, the Pond and the Forest. Where would you like to go?")
    if pine == ('blacksmith'):
        input ("You decide to head to the Blacksmith.")
        if swlvl < 1:
            swlvl = 1
        input ("You Got a LVL 1 Sword!")
        pineo = input ("Where would you like to go?")
        if pineo == ('pond'):
            input("You decide to head to the pond")
            pinehelpo = input("Please help us! My son Edward was attacked by a snake! Please, go to the medic in Tau Castle and get the code from him!")
            if pinehelpo == ("i3qr"):
                input("He is saved because of you! here take this LVL 1 Armor, It will help on your quest.")
                input("You decide to go to the forest.")
                pines()
            else:
                input ("No! that's no help!")
                pines()

    elif pine == ('pond'):
        input("You decide to head to the pond")
        pinehelp = input("Please help us! My son Edward was attacked by a snake! Go to the Witch Doctor in Swamp and get the code from him!")
        pinehelpfunc()
    elif pine == ('forest'):
        input("You decide to go to the forest.")

    else:
        input ("Sorry, I'm not sure what that means")
        pines()
pines()

input ("you arise")
input ("you notice the cool, light weight of the thin sheet of fabric covering your body")
input ("darkness")
input ("silence")
input ("you light the candle aside your bed")
input ("and prepare for your day")
input ("You entered The Pines")
#1
pine = input("There's the Blacksmith, the Pond and the Forest. Where would you like to go?")


if pine == ('blacksmith'):
    input ("You decide to head to the Blacksmith.")
    swlvl = 1
    input ("You Got a LVL 1 Sword!")
    pineo = input ("Where would you like to go?")
    if pineo == ('pond'):
        input("You decide to head to the pond")
    pinehelpo = input("Please help us! My son Edward was attacked by a snake! Please, go to the medic in Ton Castle and get the code from him!")
    if pinehelpo == ("i3qr"):
        input("He is saved because of you! here take this LVL 1 Armor, It will help on your quest.")
        input("You decide to go to the forest.")
       #Go to #1
    if pinehelpo != ("i3qr")
        input ("No! that's no help!")
        #Go to #1

if pine == ('pond'):
    input("You decide to head to the pond")
    pinehelp = input("Please help us! My son Edward was attacked by a snake! Go to the medic in Ton Castle and get the code from him!")
    if pinehelp == ("i3qr"):
        input("He is saved because of you! here take this LVL 1 Armor, It will help on your quest.")
    else:
        input ("That's no help!")
        pinehelp

if pine == ('forest'):
    input("You decide to go to the forest.")
    di = input("Ton Castle is infront of you, Deeper Woods are to your right, The Pines are behind you, and The Mountains are to your left")
if di == ("up"):
    input("You Decide to head upward")
if di == ("right"):
    input("You Decide to head right")
if di == ("left"):
    input("You Decide to head left")
if di == ("down"):
    input("You Decide to head downward")

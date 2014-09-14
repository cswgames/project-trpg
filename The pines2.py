input ("You arise")
input ("you notice the cool, light weight of the thin sheet of fabric covering your body")
input ("darkness")
input ("silence")
input ("you light the candle aside your bed")
input ("and prepare for your day")
input ("You enter The Pines")
#1
def pinehub():
    pine = input("There's the Blacksmith, the Pond and the Forest. Where would you like to go?")
    pinep = [['blacksmith','pond','forest']]

    if pine is not in pinep:
        input ("lol")
        pinehub()
    pinehub()
pinehub()

    if pine == ('blacksmith'):
        input ("You decide to head to the Blacksmith.")
        if swlvl < 1:
            swlvl = 1
            input ("You Got a LVL 1 Sword!")
        else:
            input("You already have this sword!")
    elif pine == ('pond'):
        input("You decide to head to the pond")
    pinehelpo = input("Please help us! My son Edward was attacked by a snake! Please, go to the medic in Tau Castle and get the code from him!")
        if pinehelpo == ("i3qr"):
        input("He is saved because of you! here take this LVL 1 Armor, It will help on your quest.")
        input("You decide to go to the forest.")    #Go to #1
    if pinehelpo != ("i3qr"):
        input ("No! that's no help!")
        #Go to #1

    if pine == ('forest'):
        input("You decide to go to the forest.")
        di = input("Tau Castle is infront of you, the deep woods are to your right, The Pines are behind you, and the mountains are to your left")
        if di == ("up"):
            input("You Decide to head forward, to Tau Castle")
        if di == ("right"):
            input("You Decide to head right, into the Deep Woods")
        if di == ("left"):
            input("You Decide to head left, into the mountain ranges")
        if di == ("down"):
            input("You Decide to head downward")

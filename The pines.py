input ("you arise")
input ("the cool, light weight of a thin sheet of fabric covers your body")
input ("darkness")
input ("silence")
input ("you switch on your bedside lamp")
input ("you proceed with your day")
input ("You've entered The Pines")
pine = input("Tehre's the Blacksmith, The Pond and Forest. Where would you like to go?")


if pine == ('blacksmith'):
    input ("You decide to head to the Blacksmith.")
    input ("You Got a LVL 1 Sword!")
    pineo = input ("Where would you like to go?")
    if pineo == ('pond'):
        input("You decide to head to the pond")
    pinehelpo = input("Please help us! My son Edward was attacked by a snake! Go to the medic in Ton Castle and get the code from him!")
    if pinehelpo == ("i3qr"):
        input("He is saved because of you! here take this LVL 1 Armor, It will help on your quest.")
        input("You decide to go to the forest.")
        di = input("Ton castle up, Deeper woods right, The Pines back, The mountains left")
        if di == ("up"):
            input("You Decide to head upward")
        if di == ("right"):
            input("You Decide to head right")
        if di == ("left"):
            input("You Decide to head left")
        if di == ("down"):
            input("You Decide to head downward")


if pine == ('pond'):
    input("You decide to head to the pond")
    pinehelp = input("Please help us! My son Edward was attacked by a snake! Go to the medic in Ton Castle and get the code from him!")
    if pinehelp == ("i3qr"):
        input("He is saved because of you! here take this LVL 1 Armor, It will help on your quest.")
        piner = input("Where would you like to go?")
        if piner == ('blacksmith'):
            input ("You decide to head to the Blacksmith.")
            input ("You Got a LVL 1 Sword!")
            input("You decide to go to the forest.")
            di = input("Ton castle up, Deeper woods right, The Pines back, The mountains left")
            if di == ("up"):
                input("You Decide to head upward")
            if di == ("right"):
                input("You Decide to head right")
            if di == ("left"):
                input("You Decide to head left")
            if di == ("down"):
                input("You Decide to head downward")


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

def caveswagg():
    input("You decide to head into the dark cave.")
    cavety = input("It's Dark. You decide that there is no going back. Do you want to keep going or leave while you have the chance? Type 'leave' or 'keep going' >").strip().lower()
    if cavety == "leave":
        input("You leave the cave.")
    elif cavety == "keep going":
        input("You decide to keep going.")
    else:
        input("I do not understand")
    caveswagg()
caveswagg()

def cavesavee():
    cavety2 = input("You travel deep into the cave, you hit a wall and there is a split hall, Do you go right or left? >")
    if cavety2 == "left":
        input("You head over to the left")
        input("You start to see light, you continue. You find a Treasure Chest. Inside you found a LVL 3 Bow!")
        input("You now leave the cave.")
         #Give a LVL 3 Bow to player
    elif cavety2 == "right":
        input("You head over to the right.")
        input("You see light, you continue foward. As you are walking you feel a sharp pain in your back. The blade is pulled out from your spine. You fall down.")
        input("GAME OVER")
    else:
        input("I do not understand")
    cavesavee()
cavesavee()


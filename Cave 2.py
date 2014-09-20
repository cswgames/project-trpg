def cavesaresofunright():
    print("You head into a dark cave.")
    swegswegjopper = input("As you walking you realize that there is a torch in the wall. Do you want to take it or go without it? [Type take or no] > ").strip().lower()
    if swegswegjopper == "take":
        input("As you take the torch you feel the ground shaking. You start to run but it is to late. Your body is crushed by a large boulder.")
        input("GAMEOVER")
        #load the main menu
    elif swegswegjopper == "no":
        input("You decide that it is safer to go without it. Who knows, it might be a trap.")
        input("As you walk through the cave you find a old book.")
        input('The book reads, "TELL THE GOLDEN DOOR ON TORCH ISLAND THIS CODE. yfws7"')
        input("You now leave the cave.")
        #The golden door has the best armor in the game, LVL 10
        #load the road funct
    else:
        print("I am sorry, please say that again.")
        cavesaresofunright()







cavesaresofunright()       



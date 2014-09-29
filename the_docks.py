def disdockdock():
    dipdorpdop = input("Welcome to the Docks, Would you like to set sail? or go back to the road? [Type 'sail' or 'road'] >").strip().lower()
    if dipdorpdop == "sail":
        wheredoyouwannasaillahore()

    elif dipdorpdop == "road":
        print("You leave the docks.")
        #load road funct.

    else:
        print("I am sorry, I do not understand.")
        disdockdock()        

def wheredoyouwannasaillahore():
    williamhastomuchswag = input('"Hello there mate! Would you like to go to Torch island? or The Five Islands?" [Type "torch" or "five".]').strip().lower()

    if williamhastomuchswag == "torch":
        input('"Alright! I wish you safe travels." The boat sails off.')

    elif williamhastomuchswag == "five":
        input('"Alright! I wish you safe travels." The boat sails off.')

    else:
        print("What did you say?")
        wheredoyouwannasaillahore()



disdockdock()

def fiveislands():
    fiveisyn = input("Are you sure that you'd like to begin this side quest?(Y/N)").strip().title()
    if fiveisyn == ("N"):
        input("You turn back.")
        #this depends on where we put the entrance.
    elif fiveisyn == ("Y"):
        fiveis()
    else:
        print ("I'm sorry, I'm not sure what that means, answer Y for yes or N for no.")
        fiveislands()
#----------------------------------------------------------------------------------
def fiveis():
    input("You set out to sea, the calmness of the water is relaxing and soothing.").strip().lower()
    input("In all directions water is the only thing visible.")
    fiveisyn = input("You see land, sail towards land? (Y/N)")
    if fiveisyn == "y":
        print("You start to sail towards the island.")
        fiveisarrive()
    elif fiveisyn == "n":
        print("You begin to sail back to the land you came from.")
        fiveisarrive()
    else:
        print ("I'm sorry, I'm not sure what that means, answer Y for yes or N for no.")
        fiveis()
#----------------------------------------------------------------------------------
def fiveisarrive():
    print("The wind picks up")
    print("Rain pounds against the water.")
    print("The crashing waves are too much for the little boat.")
    print("You pass out...")
    print("...darkness...")
    print("...blackness...")
    print("You awaken, dazed and confused.")
    print("You see the remains of what you assume is a sailboat, lying on the ground next to you, damaged beyond repair.")
    


fiveislands()

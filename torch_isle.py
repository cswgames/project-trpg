def torchisshore():
    torchislandsk = input("You arive at this large island It has a volcano, surrounded by the jungle. Would you like to head to the jungle? Explore the beach? or Sail back.[Type 'sail,'beach','jungle'").strip().lower()
    if torchislandsk == "sail":
        input("Knowing the danger ahead you decide to head back.")
        #load dock funct.
    elif torchislandsk == "beach":
        input("You decide to head to the beach")
        contbeach()
    elif torchislandsk == "jungle":
        input("You decide to go to the jungle")
        contjung()
    else:
        print("I'm sorry, Let me ask you again.")
        torchisshore()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def contbeach():
    mrbeachhassweg = input("You walk along the beach when you see strange foot prints on the sand.... do you want to follow? or keep walking foward? [Type 'follow' or 'continue']").strip().lower()
    if mrbeachhassweg == "follow":
        footsteps_torch()
    elif mrbeachhassweg == "continue":
        pass
    else:
         print("I'm sorry, Let me ask you again.")
         contbeach()


def contjung():
    jungisfumkids = input("You head deep into the jungle and encounter mossy ruins. Would you like to go in? or stay on the trail? [Type 'go' or 'stay'] >").strip().lower()
    if jungisfumkids == "go":
        pass #load ruins funct
    elif jungisfumkids == "stay":
        pass
    else:
         print("I'm sorry, Let me ask you again.")
         contjung()



def footsteps_torch():
        pass

def




torchisshore()

#Jack made this, William you need to do the add points thing like you did in the pines  here.

def farmhub():
        frub = input("Welcome to Micheals farm, Here we have a, Farm, Cornfield or back on the road, Where do you want to go? > ").strip().lower()
        if frub == "farm":
                input("You decide to head to the farm.")
                mikeconvosweg()
        else:
                print("I don't Understand. What did you say?")
                farmhub()

                
def mikeconvosweg():
        mikeiscool = input('"Hello there! Did you come to help me work?" [Type yes or no]').strip().lower()
        if mikeiscool == ("no"):
                input("Ok then, goodbye.")
        elif mikeiscool == ("yes"):
                input("Ok good, now I want you to go to the Cornfield and pick me the golden corn from")
        else:
                print('"What did you say?" [type yes or no]')
                mikeconvosweg()



farmhub()




      

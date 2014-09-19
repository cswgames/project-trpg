#Jack made this, William you need to do the add points thing like you did in the pines  here.

def farmhub():
        frub = input("Welcome to Micheals farm, Here we have a, Farm, Cornfield or back on the road, Where do you want to go? > ").strip().lower()
        if frub == "farm":
                input("You decide to head to the farm.")
                mikeconvosweg()

        elif frub == "road":
                input("You decide to head back on the road.")
                #load the road function....... that we dont have yet :D
        elif frub == "cornfield":
                print("You decide to head to the cornfield.")
                #load the cornfield function that soren has made.
        else:
                print("I don't Understand. What did you say?")
                farmhub()
        
                
def mikeconvosweg():
        mikeiscool = input('"Hello there! Did you come to help me work?" [Type yes or no]').strip().lower()
        if mikeiscool == ("no"):
                input("Ok then, goodbye.")
                farmhub()
        elif mikeiscool == ("yes"):
                input("Ok good, now I want you to go to the Cornfield and pick me the golden corn from the back of the field.")
                mikeisacode = input("If you already have the code, enter it here. If not, just give Micheal a random answer.").strip().lower()
                if mikeisacode == "w6rte":
                        print('"Thanks! Here is your payment."')
                        input("You got LVL 2 Armor!")
                        farmhub()
                        #Do the add 1 point thing William
                else:
                        print("I am sorry, please tell me another time. See you later!")
                        farmhub()
        else:   
                print('"What did you say?" [type yes or no]')
                mikeconvosweg()



farmhub()




      

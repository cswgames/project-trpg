#Whole thing needs != statements, Thats for you william. :D
name = input ("name needs a variable so put your name in, this will only be here until we put all these parts in the final product.").strip().title()
input("Welcome to Tau Castle.")
tau = input("Here we have a market, Royal hall, blacksmith, prison and the road. Where would you like to go?").strip().lower()
if tau == ("blacksmith"):
    input("You decide to go to the Blacksmith")
    taub = input("Mega deal! What would you like a better sword (LVL 2) or a bow(LVL 1)?").strip().lower()
    if taub == ("sword"):
        input("One sword for you " + name)
    if taub == ("bow"):
        input("One bow for you " + name)


if tau == ("market"):
    input("You decide to go to the market.")
    taucha = input("Just as you are looking at the food you hear a loud scream, and a man running. Theif! Do you want to chase him or back off?").strip().lower()
    if taucha == ("chase"):
        input("You decide to chase after the theif")
        #Combat section once we get that, prize LVL 2 armor
    if taucha == ("back off"):
        input("You decide to back off")
        #No prize


if tau == ("prison"):
    input("You decide to go to the Prison.")
    taupris = input ("Hey, I know where a lot of treasure is. You help me escape, and we will split it. Y/N").strip().lower()
    if taupris == ("y"):
        input("Thank you so much! First thing you need to do is get the code from the royal hall, then come back and enter the code and we will be on our way!")
        ("If you know the code type it in here, if you don't know it type in bye")
        
        
    
          

    

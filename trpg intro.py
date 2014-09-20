input ('''                   CSWGAMES PRESENTS......''')
input ('''
 \_\_\_\_\_  \_          \_\_\_\_\_  \_      \_  \_\_\_\_\_
  \_      \_  \_          \_      \_  \_      \_  \_      \_
   \_\_\_\_\_  \_          \_\_\_\_\_  \_\_\_\_\_  \_\_\_\_\_
    \_      \_  \_          \_          \_      \_  \_      \_
     \_      \_  \_          \_          \_      \_  \_      \_
      \_      \_  \_\_\_\_\_  \_          \_      \_  \_      \_

        \_\_\_\_\_  \_      \_  \_\_\_\_\_  \_\_\_\_\_  \_\_\_\_\_
         \_      \_  \_      \_  \_          \_              \_
          \_      \_  \_      \_  \_\_\_      \_\_\_\_\_      \_
           \_      \_  \_      \_  \_                  \_      \_
            \_      \_  \_      \_  \_                  \_      \_
             \_\_\_\_\_  \_\_\_\_\_  \_\_\_\_\_  \_\_\_\_\_      \_''')


def mainmenuaq():
    mainmyt = input("Type 'start' for new game. Type 'help' for things you might not understand. Type 'cred' to see all the people who helped make this game.").strip().lower()
    if mainmyt == "start":
        print("You are now playing Alpha Quest. Enjoy!")
        namein()

    if mainmyt == "help":
        print("Alpha Quest runs on, Windows, Mac OS X and Linux/UNIX. Just remember that you will need Python, [what this game is coded in] installed on the computer.")
        print()
        print("You cannot save your game.  Alpha Quest has no main story, but many sidequests. It is up to the player to find out what gear they want to get, and what they dont want to get.")
        print()
        print("If you die, you are dead for good.")
        print()
        print("If you have any problems, tweet the problem to us on twitter @cswgames")
        mainmenuaq()

    if mainmyt == "cred":
        input("add credits in once game is done.")
        mainmenuaq()


def namein():
    name = input(''' So now, What's your name?
    >>>''').strip().title()
    yn = input('Oh! So your name is ' + name +' right? (Y/N)').strip().title()
    if yn == ('Y'):
        print ('''GAME START''')
        #Load the pines
        
    elif yn == ('N'):
        input("Oh?")
        input("So that's not your name?")
        input("Well then...")
        input("I suppose we could sit here for a while and do nothing")
        input("Or instead, here's an idea, you could tell me your REAL name!")
        input("Sound good?")
        namein()
    else:
        input("Sorry, I don't know what that means, answer Y for yes or N for no")
        namein()


mainmenuaq()

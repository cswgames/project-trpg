input ('''                   Hello! And welcome to''')
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
def namein():
    name = input('''What's your name?
    >>>''').strip().title()
    nameout()
def nameout():
    yn = input('Oh! So your name is ' +name +' right? (Y/N)').strip().title()
    if yn == ('Y'):
        print ('''GAME START''')
        input ("You arise")
        input ("you notice the cool, light weight of the thin sheet of fabric covering your body")
        input ("darkness")
        input ("silence")
        input ("you light the candle aside your bed")
        input ("and prepare for your day")
        pines()
    elif yn == ('N'):
        input("Oh?")
        input("So that's not your name?")
        input("Well then...")
        input("I suppose we could sit here for a while and do nothing")
        input("Or instead, here's an idea, you could tell me your REAL name!")
        input("Sound good?")
        namein()
    else yn != ('N','Y'):
        input("Sorry, I don't know what that means, answer Y for yes or N for no")
        nameout()
################################################################################
def caveswagg():
    input("You decide to head into the dark cave.")
    cavety = input("It's Dark. You decide that there is no going back. Do you want to keep going or leave while you have the chance? Tpye 'leave' or 'keep going' >").strip().lower()
    if cavety == "leave":
        input("You leave the cave.")
    elif cavety == "keep going":
        input("You decide to keep going.")
    else:
        input("I do not understand")
#--------------------------------------------------------------------------------
def cavesavee():
    cavety2 = input("You travel deep into the cave, you hit a wall and there is a split hall, Do you go right or left? >")
    if cavety2 == "left":
        input("You head over to the left")
        input("You start to see light, you continue. You find a Treasure Chest. Inside you found a LVL 3 Bow!")
        input("You now leave the cave.")
        if bolvl < 3:
            bowlvl = 3
        else:
            input("You don't want none of this.")
    elif cavety2 == "right":
        input("You head over to the right.")
        input("You see light, you continue foward. As you are walking you feel a sharp pain in your back. The blade is pulled out from your spine. You fall down.")
        input("GAME OVER")
    else:
        input("I do not understand")
    cavesavee()
        

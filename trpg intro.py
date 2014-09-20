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

namein()

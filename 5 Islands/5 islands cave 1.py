input("You proceed into the deep, dark cave")
input("You walk along, huggung the wall")
def islescave():
    iscavetorch = input("You find a torch, would you like to take it?").strip().lower()
    if iscavetorch == "yes":
        input("You take the torch with you")
        islescavelrtorch()
    elif torch == "no":
        islescavelrnotorch()
    else:
        islescave()
def iscavelrtorch():
    iscavelr = input("You come to an fork in the path, do you wish to go left or right?").strip().title()
    if iscavelr == "right":
        yougoleft()
    elif 5iscavelr == "left":
        yougoright()
    else:
        iscavelrtorch()
def iscavelrnotorch

lra=[["L","R"]]
def fun():
    lr=input("lr?").strip().upper()
    if lr=="L":
        print("You decide to head left")
    elif lr=="R":
        print("You decide to head Right")
    else:
        input("I am sorry, I do not understand")
    fun()
fun()
    
    

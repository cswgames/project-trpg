def mikeconvosweg():
        mikeiscool = input('"Hello there! Did you come to help me work?" [Type yes or no]').strip().lower()
        if mikeiscool == ("no"):
                input("Ok then, goodbye.")
        elif mikeiscool == ("yes"):
                input("Ok good, now I want you to go to the Cornfield and pick me the golden corn from")
        else:
                print('"What did you say?" [type yes or no]')
        mikeconvosweg()
mikeconvosweg()

def loginfo(texto):
    f = open("Seven_and_Half_LOG.txt", "a")
    f.write(text)
    f.close()

def management_menu(title="",options=[]):
    while True:
        if title == "":
            print(title.center(50,"="))
        for i in range(len(options)):
            aux = str(i+1) + ") " + options[i]
            print(aux.center(50))
        option = input("Option: ".rjust(29))
        print()
        if not option.isdigit():
            print("Invalid Option".center(50,"="))
        elif int(option) not in range(1,len(options)+1):
            print("Invalid Option".center(50,"="))
        else:
            return int(option)
        print()
        input("Press enter to continue")
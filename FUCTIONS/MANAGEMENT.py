def loginfo(texto):
    f = open("Seven_and_Half_LOG.txt", "a")
    f.write(texto)
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

def newrandomdni():
    letras_dni = ["T", "R", "W", "A", "G", "M", "Y",
                  "F", "P", "D", "X", "B", "N", "J",
                  "Z", "S", "Q", "V", "H", "L", "C",
                  "K", "E"]
    while True :
        dni = input("Introduce your ID: ")
        if not dni[0:8].isdigit():
            print("The DNI only can contain eight numbers and one letter.".center(50))
        elif dni[8].upper() != letras_dni[int(dni[0:8]) % 23]:
            print("The letter is incorrect.".center(50))
        else:
            return dni.upper()
        print()
        input("Press enter to continue".center(50))
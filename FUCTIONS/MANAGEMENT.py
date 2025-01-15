def loginfo(texto):
    f = open("Seven_and_Half_LOG.txt", "a")
    f.write(texto)
    f.close()

def management_menu(title=1,menu=()):
    while True:
        if title >= 1:
            print("".center(50,"="))
            for i in range(title):
                print(menu[i].center(50))
            print("".center(50,"="))
        for i in range(title,len(menu)):
            aux = str(i-title//2) + ") " + menu[i]
            print(aux.center(50))
        option = input("Option: ".rjust(29))
        print()
        if not option.isdigit():
            print("Invalid Option".center(50,"="))
        elif int(option) not in range(1,len(menu)-title//2):
            print("Invalid Option".center(50,"="))
        else:
            loginfo("\nEl jugador a elegido una opcion")
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
            loginfo("\nSe a creado un nuevo ID")
            return dni.upper()
        print()
        input("Press enter to continue".center(50))
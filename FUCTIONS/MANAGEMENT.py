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

def rondamaxima():
    ronda = input("Introduce el maximo de rondas (del 1 al 30):".rjust(29))
    if not ronda.isdigit():
        print("Debe ser un numero".center(50))
    elif int(ronda) not in range(1,31):
        print("Debe ser un numero del 1 al 30".center(50))
    else:
        return ronda
    print()
    input("Press enter to continue")
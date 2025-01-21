import gestionar_juego as funcion_juego
import os
#Crear automaticamente menus y pedir opciones.
def management_menu(title=1,menu=()):
    while True:
        print()
        if title >= 1:
            print("".center(50,"="))
            for i in range(title):
                print(menu[i].center(50))
            print("".center(50,"="))
        for i in range(title,len(menu)):
            aux = str(i-title//2) + ") " + menu[i]
            print(aux.center(50))
        option = input("Opcion: ".rjust(30))
        print()
        if not option.isdigit():
            print("Opcion invalida".center(50,"="))
        elif int(option) not in range(1,len(menu)-title//2):
            print("Opcion invalida".center(50,"="))
        else:
            funcion_juego.loginfo("El jugador a elegido una opcion")
            return int(option)
        print()
        input("Presiona enter para continuar".center(50))


def clearscreen():
    # Verificamos si el sistema operativo es Windows o no
    if os.name == "nt":
        # Para Windows
        _ = os.system("cls")
    else:
        # Para otros sistemas operativos (Linux, macOS)
        _ = os.system("clear")

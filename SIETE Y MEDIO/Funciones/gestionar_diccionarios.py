import Funciones.gestionar_interfaz as interface
import Funciones.gestionar_base_de_datos as bbdd

#Elegir la ronda maxima.
def rondamaxima():
    while True:
        ronda = input("Introduce el maximo de rondas (del 1 al 30):".rjust(29))
        if ronda.replace(" ","") == "":
            ronda = "5"
            return int(ronda)
        if not ronda.isdigit():
            print("Debe ser un numero".center(50))
        elif int(ronda) not in range(1,31):
            print("Debe ser un numero del 1 al 30".center(50))
        else:
            return int(ronda)
        print()
        input("Press enter to continue")

def showplayer(player_dicto):
    pag = 0
    while True:
        lista_users = []
        for key in player_dicto:
            lista_users.append(key)
        print()
        print("Ver/Eliminar jugadores".center(50, "="))
        for i in range(pag * 10, min((pag + 1) * 10, len(lista_users))):
            aux = str(i+1) + ") " + lista_users[i]
            print(aux.center(50))
        print()
        elegir = input("Elimina jugadores (-num), avanza (+) o retrocede (-), y 0 para salir: ".rjust(30))
        print()
        if elegir == "+":
            if (pag + 1) * 10 < len(player_dicto):
                pag += 1
                print("Cambio de pagina".center(50))
            else:
                print("No hay mas paginas hacia delante".center(50))
        elif elegir == "-":
            if pag > 0:
                pag -= 1
                print("Cambio de pagina".center(50))
            else:
                print("No hay mas paginas hacia atras".center(50))
        elif elegir.startswith("-") and elegir[1:].isdigit():
            if int(elegir[1:]) - 1 in range(len(player_dicto)):
                bbdd.delBBDDPlayer(lista_users[int(elegir[1:])-1])
                del player_dicto[lista_users[int(elegir[1:])-1]]
                lista_users.remove(lista_users[int(elegir[1:])-1])
                print("Se a eliminado a un jugador".center(50))
            else:
                print("No existe el jugador".center(50))
        elif not elegir.isdigit():
            print("Debe ser 0, -num, - o +".center(50))
        elif int(elegir) == 0:
            return
        else:
            print("Opcion incorrecta".center(50))
        print()
        input("Press enter to continue".rjust(30))

def nuevohumano(player_dicto):
    letras_dni = ("T", "R", "W", "A", "G", "M", "Y",
                  "F", "P", "D", "X", "B", "N", "J",
                  "Z", "S", "Q", "V", "H", "L", "C",
                  "K", "E")
    while True:
        print("".center(50,"="))
        print("New Human Player".center(50))
        print("".center(50,"="))
        print()
        name = input("Name: ".rjust(30))
        aux = name.replace(" ","")
        if not aux.isalpha():
            print("Solo puede contener letras y espacios".center(50))
        else:
            while True:
                nif = input("Nif: ".rjust(30))
                print()
                if nif in player_dicto:
                    print("El NIF ya existe")
                elif not nif[0:7].isdigit():
                    print("Los primeros 8 caracteres deben ser numeros".center(50))
                elif letras_dni[int(nif[0:7])%23] != nif[8]:
                    print("La letra no es la correcta".center(50))
                else:
                    profiles = ("Select your Profile:","Cauteloso","Moderado","Arriesgado")
                    profile = interface.management_menu(title=1,menu=profiles)
                    aux = input("Estas seguro? S/N: ".rjust(30))
                    if aux.upper() == "S":
                        player_dicto[nif]= {
                                "Name": name,
                                "Risk": profile,
                                "Type": "Humano",
                                "Puntos": 20,
                                "Minutos_Jugados": 0,
                                "In_Game": False
                            }
                    return

def nuevobot(player_dicto):
    letras_dni = ("T", "R", "W", "A", "G", "M", "Y",
                  "F", "P", "D", "X", "B", "N", "J",
                  "Z", "S", "Q", "V", "H", "L", "C",
                  "K", "E")
    while True:
        print("".center(50,"="))
        print("New Human Player".center(50))
        print("".center(50,"="))
        print()
        name = input("Name: ".rjust(30))
        while True:
            nif = input("Nif: ".rjust(30))
            print()
            if nif in player_dicto:
                print("El NIF ya existe")
            elif not nif[0:7].isdigit():
                print("Los primeros 8 caracteres deben ser numeros".center(50))
            elif not letras_dni[int(nif[0:7])%23] != nif[8]:
                print("La letra no es la correcta".center(50))
            else:
                profiles = ("Select your Profile:","Cauteloso","Moderado","Arriesgado")
                profile = interface.management_menu(title=1,menu=profiles)
                aux = input("Estas seguro? S/N: ".rjust(30))
                if aux.upper() == "S":
                    player_dicto[nif]= {
                            "Name": name,
                            "Risk": profile,
                            "Type": "Bot",
                            "Puntos": 20,
                            "Minutos_Jugados": 0,
                            "In_Game": False
                        }
                return
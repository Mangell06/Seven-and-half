import gestionar_interfaz as interface
import gestionar_base_de_datos as bbdd
import random

#Elegir la ronda maxima.
def rondamaxima():
    while True:
        ronda = input("Introduce el maximo de rondas (del 1 al 30):".rjust(29))
        print()
        if ronda.replace(" ","") == "":
            ronda = "5"
            mensaje = "El maximo de rondas de la partida ahora son {} rondas".format(ronda)
            print(mensaje.center(50))
            print()
            input("Presiona enter para continuar".center(50))
            return int(ronda)
        if not ronda.isdigit():
            print("Debe ser un numero".center(50))
        elif int(ronda) not in range(1,31):
            print("Debe ser un numero del 1 al 30".center(50))
        else:
            mensaje = "El maximo de rondas de la partida ahora son {} rondas".format(ronda)
            print(mensaje.center(50))
            print()
            input("Presiona enter para continuar".center(50))
            return int(ronda)
        print()
        input("Presiona enter para continuar")

def showplayer(player_dicto):
    pag = 0
    while True:
        lista_users = []
        for key in player_dicto:
            lista_users.append(key)
        print()
        print("Ver/Eliminar jugadores".center(50, "="))
        print()
        print("".center(50,"="))
        print( "".ljust(5) + "NIF".ljust(15) + "NAME".ljust(15) + "TYPE".rjust(15))
        for i in range(pag * 10, min((pag + 1) * 10, len(lista_users))):
            print("{})".format(str(i+1)).ljust(5) + lista_users[i].ljust(15) + player_dicto[lista_users[i]]["Name"].ljust(15) + player_dicto[lista_users[i]]["Type"].rjust(15))
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
        input("Presiona enter para continuar".center(50))

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
        elif len(name) > 10 or len(name) < 1:
            print("El nombre debe medir entre 1 a 10 caracteres maximo.".center(50))
        else:
            while True:
                nif = input("Nif: ".rjust(30))
                print()
                if nif in player_dicto:
                    print("El NIF ya existe")
                elif not nif[0:8].isdigit():
                    print("Los primeros 8 caracteres deben ser numeros".center(50))
                elif letras_dni[int(nif[0:8])%23] != nif[8]:
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
        print("New Bot Player".center(50))
        print("".center(50,"="))
        print()
        name = input("Name: ".rjust(30))
        if len(name) > 10 or len(name) < 1:
            print("El nombre debe medir entre 1 a 10 caracteres maximo.".center(50))
        else:
            while True:
                num = random.randint(11111111,99999999)
                letra = letras_dni[num%23]
                nif = str(num) + letra
                print()
                if nif not in player_dicto:
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
import datetime
import random
import gestionar_interfaz

#Escribir texto en el LOGS.txt como debugger
def loginfo(texto):
    with open("Logs.txt", "a") as f:
        fecha_y_hora = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        f.write(f"{fecha_y_hora} {texto}\n")

def elegirpersonajejugar(players_dict):
    disponibles = []
    jugando = []
    for player in players_dict:
        if players_dict[player]["In_Game"]:
            jugando.append(player)
        else:
            disponibles.append(player)
    pag = 0
    while True:
        print()
        print("Jugadores Disponibles:".center(50, "="))
        for i in range(pag * 10, min((pag + 1) * 10, len(disponibles))):
            aux = str(i + 1) + ") " + players_dict[disponibles[i]]["Name"]
            print(aux.center(50))
        print()
        print("Jugadores Jugando:".center(50, "="))
        for i in range(pag * 10, min((pag + 1) * 10, len(jugando))):
            aux = str(i + 1) + ") " + players_dict[jugando[i]]["Name"]
            print(aux.center(50))
        print()
        elegir = input("Añade (num), elimina jugadores (-num), avanza (+) o retrocede (-), y 0 para salir: ".rjust(30))
        print()
        if elegir == "+":
            if (pag + 1) * 10 < len(disponibles) or (pag + 1) * 10 < len(jugando):
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
            if int(elegir[1:]) - 1 in range(len(jugando)):
                disponibles.append(jugando[int(elegir[1:]) - 1])
                jugando.remove(jugando[int(elegir[1:]) - 1])
                print("Nuevo jugador disponible".center(50))
            else:
                print("No existe el jugador".center(50))
        elif not elegir.isdigit():
            print("Debe ser un numero o -num".center(50))
        elif int(elegir) == 0:
            return jugando
        elif len(jugando) == 6:
            print("Ya tienes el maximo de jugadores (6)".center(50))
        elif int(elegir) - 1 in range(len(disponibles)):
            jugando.append(disponibles[int(elegir) - 1])
            disponibles.remove(disponibles[int(elegir) - 1])
            print("Nuevo jugador jugando".center(50))
        else:
            print("No existe el jugador".center(50))
        print()
        input("Presiona enter para continuar".center(50))

def rondamaxima():
    while True:
        print()
        ronda = input("Introduce el maximo de rondas (del 1 al 30): ".rjust(30))
        print()
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
        input("Presiona enter para continuar".center(50))

def crearmazo(party_dicto,newparty_dicto,cartas):
    mazo = []
    for key in cartas:
        if newparty_dicto[len(party_dicto) + 1]["Mazo"] == "Española":
            if key[0] == "E":
                mazo.append(key)
        else:
            if key[0] == "P":
                mazo.append(key)
    return mazo

def raking_minuts_played(personajes_dict):
    lista_ordenar = list(personajes_dict.keys())
    for pasadas in range(len(lista_ordenar)):
        cambios = False
        for i in range(len(lista_ordenar) - 1 - pasadas):
            if personajes_dict[lista_ordenar[i]]["Minutos_Jugados"] < personajes_dict[lista_ordenar[i + 1]]["Minutos_Jugados"]:
                lista_ordenar[i], lista_ordenar[i + 1] = lista_ordenar[i + 1], lista_ordenar[i]
                cambios = True
        if not cambios:
            break
    pag = 0
    while True:
        print()
        header_rank_ch = "ID".ljust(10) + "Name".ljust(15) + "Risk".ljust(10) + "Type".ljust(12) + "Puntos".rjust(10) + "Minutos Jugados".rjust(18)
        print(header_rank_ch)

        for i in range(pag * 10, min((pag + 1) * 10, len(lista_ordenar))):
            ID = lista_ordenar[i]
            personaje = personajes_dict[ID]
            print(str(ID).ljust(10) + personaje["Name"].ljust(15) + str(personaje["Risk"]).ljust(10) + personaje["Type"].ljust(12) + str(personaje["Puntos"]).rjust(10) + str(personaje["Minutos_Jugados"]).rjust(18))

        elegir = input("Avanza (+) o retrocede (-), y 0 para salir: ".rjust(30))
        if elegir == "+":
            if (pag + 1) * 10 < len(lista_ordenar):
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
        elif elegir == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.".center(50))
        input("Presiona enter para continuar".center(50))

def raking_id(personajes_dict):

    lista_ordenar = list(personajes_dict.keys())

    for pasadas in range(len(lista_ordenar)):
        cambios = False
        for i in range(len(lista_ordenar) - 1 - pasadas):
            if lista_ordenar[i] > lista_ordenar[i + 1]:
                lista_ordenar[i], lista_ordenar[i + 1] = lista_ordenar[i + 1], lista_ordenar[i]
                cambios = True
        if not cambios:
            break

    pag = 0
    while True:
        print()
        header_rank_ch = "ID".ljust(10) + "Name".ljust(15) + "Risk".ljust(10) + "Type".ljust(12) + "Puntos".rjust(10) + "Minutos Jugados".rjust(18)
        print(header_rank_ch)

        for i in range(pag * 10, min((pag + 1) * 10, len(lista_ordenar))):
            ID = lista_ordenar[i]
            personaje = personajes_dict[ID]
            print(str(ID).ljust(10) + personaje["Name"].ljust(15) + str(personaje["Risk"]).ljust(10) + personaje["Type"].ljust(12) + str(personaje["Puntos"]).rjust(10) + str(personaje["Minutos_Jugados"]).rjust(18))

        elegir = input("Avanza (+) o retrocede (-), y 0 para salir: ".rjust(30))
        if elegir == "+":
            if (pag + 1) * 10 < len(lista_ordenar):
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
        elif elegir == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.".center(50))
        input("Presiona enter para continuar".center(50))

def raking_puntos(personajes_dict):
    lista_ordenar = list(personajes_dict.keys())

    for pasadas in range(len(lista_ordenar)):
        cambios = False
        for i in range(len(lista_ordenar) - 1 - pasadas):
            if personajes_dict[lista_ordenar[i]]["Puntos"] < personajes_dict[lista_ordenar[i + 1]]["Puntos"]:
                lista_ordenar[i], lista_ordenar[i + 1] = lista_ordenar[i + 1], lista_ordenar[i]
                cambios = True
        if not cambios:
            break

    pag = 0
    while True:
        print()
        header_rank_ch = "ID".ljust(10) + "Name".ljust(15) + "Risk".ljust(10) + "Type".ljust(12) + "Puntos".rjust(10) + "Minutos Jugados".rjust(18)
        print(header_rank_ch)

        for i in range(pag * 10, min((pag + 1) * 10, len(lista_ordenar))):
            ID = lista_ordenar[i]
            personaje = personajes_dict[ID]
            print(str(ID).ljust(10) + personaje["Name"].ljust(15) + str(personaje["Risk"]).ljust(10) + personaje["Type"].ljust(12) + str(personaje["Puntos"]).rjust(10) + str(personaje["Minutos_Jugados"]).rjust(18))

        elegir = input("Avanza (+) o retrocede (-), y 0 para salir: ".rjust(30))
        if elegir == "+":
            if (pag + 1) * 10 < len(lista_ordenar):
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
        elif elegir == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.".center(50))
        input("Presiona enter para continuar".center(50))

def crearcontext(jugadores,contexto,partidas,players):
    for key in jugadores:
        contexto[len(partidas) + 1][key] = {
            "Puntos_iniciales": players[key]["Puntos"],
            "Puntos_finales": 0,
            "Carta_inicial": ""
        }

def crearrondas(jugadores,contextorondas,partidas,players,contador):
    contadore = 0
    contextorondas[len(partidas) + 1] = {}
    contextorondas[len(partidas) + 1][contador] = {}
    for key in jugadores:
        contadore += 1
        contextorondas[len(partidas) + 1][contador][key] = {
            "Es_banca": False,
            "Prioridad": contadore,
            "Apuesta": 0,
            "Puntos_inciales": players[key]["Puntos"],
            "Valor_total_cartas": 0,
            "Cartas": []
        }


def priority(jugadores, contexto, partidas, carts,contador):
    asignadas = []
    for key in jugadores:
        carta = random.randint(0, len(carts) - 1)
        if carts[carta] not in asignadas:
            asignadas.append(carts[carta])
            contexto[len(partidas) + 1][contador][key]["Cartas"].append(carts[carta])

def selectpriority(contexto, jugadores, carts, partidas,contador):
    partida_actual = len(partidas) + 1
    jugadores_cartas = []
    for jugador in jugadores:
        carta = contexto[partida_actual][contador][jugador]["Cartas"][0]
        real_value = carts[carta]["realValue"]
        priority = carts[carta]["priority"]
        jugadores_cartas.append((jugador, carta, real_value, priority))
    jugadores_cartas.sort(key=lambda x: (x[2], x[3]))
    for idx, (jugador, carta, _, _) in enumerate(jugadores_cartas):
        contexto[partida_actual][contador][jugador]["Prioridad"] = idx + 1
    for pasadas in range(len(jugadores)):
        for i in range(len(jugadores)-1-pasadas):
            if contexto[partida_actual][contador][jugadores[i]]["Prioridad"] > contexto[partida_actual][contador][jugadores[i+1]]["Prioridad"]:
                aux = jugadores[i]
                jugadores[i] = jugadores[i+1]
                jugadores[i+1] = aux

def limpiarcartas(contexto,partidas,contador):
    for key in contexto[len(partidas) + 1][contador]:
        print(key)
        contexto[len(partidas) + 1][contador][key]["Cartas"] = []

def rondas(contador,jugador,jugadoresenpartida,jugadores):
    ronda = ("Turno {} Juega {}".format(contador,jugador),"Ver estados",
             "Ver estados de jugadores","Apostar","Pedir Carta",
             "Jugar ronda automaticamente","Pararse")
    opc = gestionar_interfaz.management_menu(title=1,menu=ronda)
    if opc == 1:
        print("Nombre".ljust(10) + jugadores[jugador]["Name"].rjust(10))
        print("Tipo".ljust(10) + jugadores[jugador]["Type"].rjust(10))
        print()
    elif opc == 2:
        print(2)
    elif opc == 3:
        print(3)
    elif opc == 4:
        print(4)
    elif opc == 5:
        print(5)
    else:
        print(6)
import datetime
import random
from traceback import print_tb

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

def crearmazo(newparty_dicto,cartas):
    mazo = []
    for key in cartas:
        if newparty_dicto["Mazo"] == "Española":
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

def crearcontext(jugadores,contexto,players):
    contador = 0
    for key in jugadores:
        contador += 1
        contexto[key] = {
            "Puntos_iniciales": players[key]["Puntos"],
            "Puntos_finales": 0,
            "Prioridad":contador,
            "Carta_inicial": ""
        }

def crearrondas(jugadores,contextorondas,players,contador):
    contextorondas[contador] = {}
    for key in jugadores:
        contextorondas[contador][key] = {
            "Es_banca": False,
            "Apuesta": 0,
            "Puntos": players[key]["Puntos"],
            "Valor_total_cartas": 0,
            "Cartas": []
        }

def priority(jugadores, contextpartida, carts):
    asignadas = []
    for key in jugadores:
        carta = random.randint(0, len(carts) - 1)
        if carts[carta] not in asignadas:
            asignadas.append(carts[carta])
            contextpartida[key]["Carta_inicial"] = carts[carta]

def cambioprioridad(contexto, cartas, jugadores,ronda,contadore):
    for pasada in range(len(jugadores)):
        for i in range(len(jugadores) - 1 - pasada):
            if int(contexto[jugadores[i]]["Carta_inicial"][2:]) > int(contexto[jugadores[i+1]]["Carta_inicial"][2:]):
                aux = jugadores[i]
                jugadores[i] = jugadores[i+1]
                jugadores[i+1] = aux
            elif int(contexto[jugadores[i]]["Carta_inicial"][2:]) == int(contexto[jugadores[i+1]]["Carta_inicial"][2:]):
                if cartas[contexto[jugadores[i]]["Carta_inicial"]]["priority"] > cartas[contexto[jugadores[i+1]]["Carta_inicial"]]["priority"]:
                    aux = jugadores[i]
                    jugadores[i] = jugadores[i+1]
                    jugadores[i+1] = aux
    contador = 0
    for key in jugadores:
        contador += 1
        contexto[key]["Prioridad"] = contador
        if contador == 1:
            ronda[contadore][key]["Es_banca"] = True

def limpiarcartas(contexto,contador):
    for key in contexto[contador]:
        contexto[contador][key]["Cartas"] = []

def rondas_players(jugadores,contador,turno,players):
    opciones = ("Ver estado", "Ver estados de los jugadores","Elegir apuesta","Pedir carta","Modo automatico","Plantarse")
    while True:
        print("".center(50,"="))
        print("Siete y medio".center(50))
        aux = "Round: {} {}".format(contador,players[jugadores[turno]]["Name"])
        print(aux.center(50,"="))
        for i in range(len(opciones)):
            aux = str(i+1) + ") " + opciones[i]
            print(aux.center(50))
        opc = input("Opcion: ".rjust(30))
        print()
        if not opc.isdigit():
            print("Opcion invalida".center(50, "="))
        elif int(opc) not in range(1, len(opciones) + 1):
            print("Opcion invalida".center(50, "="))
        else:
            loginfo("El jugador a elegido una opcion")
            return int(opc)
        print()
        input("Presiona enter para continuar".center(50))

def opciones(jugadores,turno,contador,players,ronda,partida):
    while True:
        print()
        opc = rondas_players(jugadores,contador,turno,players)
        if opc == 1:
            mostrar = "Estado de {}".format(players[jugadores[turno]]["Name"])
            print(mostrar.center(50,"="))
            mostrar = "Nombre". ljust(10) + players[jugadores[turno]]["Name"].rjust(10)
            print(mostrar.center(50))
            mostrar = "Tipo".ljust(10) + str(players[jugadores[turno]]["Risk"]).rjust(10)
            print(mostrar.center(50))
            mostrar = "Humano".ljust(10) + "True".rjust(10)
            print(mostrar.center(50))
            mostrar = "Banca".ljust(10) + str(ronda[contador][jugadores[turno]]["Es_banca"]).rjust(10)
            print(mostrar.center(50))
            mostrar = "Carta inicial".ljust(10) + partida[jugadores[turno]]["Carta_inicial"].rjust(10)
            print(mostrar.center(50))
            mostrar = "Prioridad".ljust(10) + str(partida[jugadores[turno]]["Prioridad"]).rjust(10)
            print(mostrar.center(50))
            mostrar = "Apuesta".ljust(10) + str(ronda[contador][jugadores[turno]]["Apuesta"]).rjust(10)
            print(mostrar.center(50))
            mostrar = "Puntos".ljust(10) + str(ronda[contador][jugadores[turno]]["Puntos"]).rjust(10)
            print(mostrar.center(50))
            mostrar = "Cartas".ljust(10) + str(ronda[contador][jugadores[turno]]["Cartas"]).rjust(10)
            print(mostrar.center(50))
            mostrar = "Puntos ronda".ljust(10) + str(ronda[contador][jugadores[turno]]["Valor_total_cartas"]).rjust(8)
            print(mostrar.center(50))
        elif opc == 2:
            print("Estado de jugadores".center(50, "="))
            print()
            print("Nombre".ljust(15) + "Humano".ljust(10) + "Prioridad".ljust(10) + "Tipo".ljust(10) +
                  "Banca".ljust(10) + "Apuesta".ljust(10) + "Puntos".ljust(10) +
                  "Cartas".ljust(15) + "Puntos ronda".ljust(15))
            print("=" * 120)
            for key in jugadores:
                if key not in jugadores[turno]:
                    print(players[key]["Name"].ljust(15) +
                          str(players[key]["Type"]).ljust(13) +
                          str(partida[key]["Prioridad"]).ljust(8) +
                          str(players[key]["Risk"]).ljust(10) +
                          str(ronda[contador][key]["Es_banca"]).ljust(10) +
                          str(ronda[contador][key]["Apuesta"]).ljust(10) +
                          str(ronda[contador][key]["Puntos"]).ljust(10) +
                          str(ronda[contador][key]["Cartas"]).ljust(20) +
                          str(ronda[contador][key]["Valor_total_cartas"]).ljust(15))
        elif opc == 3:
            if ronda[contador][jugadores[turno]]["Apuesta"] == 0:
                apuesta = input("Elige la apuesta: ".rjust(30))
                if not apuesta.isdigit():
                    mostrar = "La a puesta debe ser un digito del 1 al {}".format(ronda[contador][jugadores[turno]]["Puntos"])
                    print(mostrar.center(50,"="))
                if int(apuesta) <= ronda[contador][jugadores[turno]]["Puntos"] and int(apuesta) > 0:
                    ronda[contador][jugadores[turno]]["Apuesta"] = int(apuesta)
                else:
                    mostrar = "La a puesta debe ser un digito del 1 al {}".format(ronda[contador][jugadores[turno]]["Puntos"])
                    print(mostrar.center(50,"="))
            else:
                print("Ya has elegido la apuesta".center(50,"="))
        elif opc == 4:
            if ronda[contador][jugadores[turno]]["Apuesta"] == 0:
                print("Apuesta primero".center(50,"="))
        elif opc == 5:
            if ronda[contador][jugadores[turno]]["Apuesta"] == 0:
                print("Apuesta primero".center(50,"="))
        else:
            if ronda[contador][jugadores[turno]]["Apuesta"] == 0:
                print("Apuesta primero".center(50,"="))
            else:
                return
        print()
        input("Presiona enter para continuar".center(50))
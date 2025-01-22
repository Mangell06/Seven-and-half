import datetime
import random
import gestionar_interfaz as interface
import gestionar_base_de_datos as bbdd

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
            bbdd.desactivar_jugadores(disponibles)
            bbdd.activar_jugadores(jugando)
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

def crearrondas(jugadores,contextorondas,players,contador,proxima_banca=[]):
    contextorondas[contador] = {}
    contextorondas[contador]["ID_Ganador"] = ""
    for key in jugadores:
        if contador == 0:
            contextorondas[contador][key] = {
                "Es_banca": False,
                "Apuesta": 0,
                "Puntos": players[key]["Puntos"],
                "Valor_total_cartas": 0,
                "Cartas": []
            }
        else:
            if len(proxima_banca) > 0:
                if key in proxima_banca[0]:
                    contextorondas[contador][key] = {
                        "Es_banca":True,
                        "Apuesta": 0,
                        "Puntos": contextorondas[contador-1][key]["Puntos"],
                        "Valor_total_cartas": 0,
                        "Cartas": []
                    }
                else:
                    contextorondas[contador][key] = {
                        "Es_banca":False,
                        "Apuesta": 0,
                        "Puntos": contextorondas[contador-1][key]["Puntos"],
                        "Valor_total_cartas": 0,
                        "Cartas": []
                    }
            else:
                contextorondas[contador][key] = {
                    "Es_banca":contextorondas[contador-1][key]["Es_banca"],
                    "Apuesta": 0,
                    "Puntos": contextorondas[contador-1][key]["Puntos"],
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

def rondas_players(jugadores,contador,turno,players):
    opciones = ("Ver estado", "Ver estados de los jugadores","Elegir apuesta","Pedir carta","Modo automatico","Plantarse")
    while True:
        interface.clearscreen()
        for i in range(len(opciones)):
            aux = str(i+1) + ") " + opciones[i]
            print(aux.center(50))
        opc = input("Opcion: ".rjust(30))
        print()
        if opc == "":
            print("Opcion invalida".center(50, "="))
        elif not opc.isdigit():
            print("Opcion invalida".center(50, "="))
        elif int(opc) not in range(1, len(opciones) + 1):
            print("Opcion invalida".center(50, "="))
        else:
            loginfo("El jugador a elegido una opcion")
            return int(opc)
        print()
        input("Presiona enter para continuar".center(50))

def opciones(jugadores,turno,contador,players,ronda,partida,mazo,cartas):
    while True:
        print()
        print("".center(50,"="))
        print("Siete y medio".center(50))
        aux = "Round: {} {}".format(contador,players[jugadores[turno-1]]["Name"])
        print(aux.center(50,"="))
        opc = rondas_players(jugadores,contador,turno-1,players)
        if opc == 1:
            mostrar = "Estado de {}".format(players[jugadores[turno-1]]["Name"])
            print(mostrar.center(50,"="))
            mostrar = "Nombre". ljust(10) + players[jugadores[turno-1]]["Name"].rjust(10)
            print(mostrar.center(50))
            mostrar = "Tipo".ljust(10) + str(players[jugadores[turno-1]]["Risk"]).rjust(10)
            print(mostrar.center(50))
            mostrar = "Humano".ljust(10) + "True".rjust(10)
            print(mostrar.center(50))
            mostrar = "Banca".ljust(10) + str(ronda[contador][jugadores[turno-1]]["Es_banca"]).rjust(10)
            print(mostrar.center(50))
            mostrar = "Carta inicial".ljust(10) + partida[jugadores[turno-1]]["Carta_inicial"].rjust(10)
            print(mostrar.center(50))
            mostrar = "Prioridad".ljust(10) + str(partida[jugadores[turno-1]]["Prioridad"]).rjust(10)
            print(mostrar.center(50))
            mostrar = "Apuesta".ljust(10) + str(ronda[contador][jugadores[turno-1]]["Apuesta"]).rjust(10)
            print(mostrar.center(50))
            mostrar = "Puntos".ljust(10) + str(ronda[contador][jugadores[turno-1]]["Puntos"]).rjust(10)
            print(mostrar.center(50))
            mostrar = "Cartas".ljust(10) + str(ronda[contador][jugadores[turno-1]]["Cartas"]).rjust(10)
            print(mostrar.center(50))
            mostrar = "Puntos ronda".ljust(10) + str(ronda[contador][jugadores[turno-1]]["Valor_total_cartas"]).rjust(8)
            print(mostrar.center(50))
        elif opc == 2:
            print("Estado de jugadores".center(50, "="))
            print()
            print("Nombre".ljust(15) + "Humano".ljust(10) + "Prioridad".ljust(10) + "Tipo".ljust(10) +
                  "Banca".ljust(10) + "Apuesta".ljust(10) + "Puntos".ljust(10) +
                  "Cartas".ljust(15) + "Puntos ronda".ljust(15))
            print("=" * 120)
            for key in jugadores:
                if key not in jugadores[turno-1]:
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
            if ronda[contador][jugadores[turno-1]]["Apuesta"] == 0:
                apuesta = input("Elige la apuesta: ".rjust(30))
                if apuesta == "":
                    print("Asigna algun valor numerico".center(50))
                elif not apuesta.isdigit():
                    mostrar = "La a puesta debe ser un digito del 1 al {}".format(ronda[contador][jugadores[turno-1]]["Puntos"])
                    print(mostrar.center(50,"="))
                elif int(apuesta) <= ronda[contador][jugadores[turno-1]]["Puntos"] and int(apuesta) > 0:
                    ronda[contador][jugadores[turno-1]]["Apuesta"] = int(apuesta)
                else:
                    mostrar = "La a puesta debe ser un digito del 1 al {}".format(ronda[contador][jugadores[turno-1]]["Puntos"])
                    print(mostrar.center(50,"="))
            else:
                print("Ya has elegido la apuesta".center(50,"="))
        elif opc == 4:
            if ronda[contador][jugadores[turno-1]]["Apuesta"] == 0:
                print("Apuesta primero".center(50,"="))
            elif ronda[contador][jugadores[turno-1]]["Valor_total_cartas"] >= 7.5:
                print("Ya has llegado al limite".center(50,"="))
            else:
                asignadas = []
                terminar = False
                for key in jugadores:
                    for i in range(len(ronda[contador][key]["Cartas"])):
                        asignadas.append(ronda[contador][key]["Cartas"][i])
                while not terminar:
                    carta = mazo[random.randint(0,len(mazo) - 1)]
                    if carta not in asignadas:
                        ronda[contador][jugadores[turno-1]]["Cartas"].append(carta)
                        ronda[contador][jugadores[turno-1]]["Valor_total_cartas"] += cartas[carta]["value"]
                        terminar = True
        elif opc == 5:
            if ronda[contador][jugadores[turno-1]]["Apuesta"] == 0:
                print("Apuesta primero".center(50,"="))
            else:
                print("Bot")
        else:
            if ronda[contador][jugadores[turno-1]]["Apuesta"] == 0:
                print("Apuesta primero".center(50,"="))
            elif ronda[contador][jugadores[turno-1]]["Valor_total_cartas"] == 0:
                print("Elige minimo una carta".center(50,"="))
            else:
                return
        print()
        input("Presiona enter para continuar".center(50))

def ganar(contextoronda,jugadores,players,contador,contextopartida):
    proxima_banca = []
    copia = jugadores.copy()
    for pasadas in range(len(copia)-1):
        for i in range(len(copia)-1-pasadas):
            if contextoronda[contador][copia[i]]["Valor_total_cartas"] == 7.5:
                proxima_banca.append(copia[i])
            if contextoronda[contador][copia[i]]["Valor_total_cartas"] > 7.5:
                    aux = copia[i]
                    copia[i] = copia[i+1]
                    copia[i+1] = aux
            elif contextoronda[contador][copia[i]]["Valor_total_cartas"] < contextoronda[contador][copia[i+1]]["Valor_total_cartas"] and contextoronda[contador][copia[i]]["Valor_total_cartas"] <= 7.5 and contextoronda[contador][copia[i+1]]["Valor_total_cartas"] <= 7.5:
                aux = copia[i]
                copia[i] = copia[i+1]
                copia[i+1] = aux
            elif contextoronda[contador][copia[i]]["Valor_total_cartas"] == contextoronda[contador][copia[i+1]]["Valor_total_cartas"]  and contextoronda[contador][copia[i]]["Valor_total_cartas"] <= 7.5:
                if contextopartida[copia[i]]["Prioridad"] > contextopartida[copia[i+1]]["Prioridad"]:
                    aux = copia[i]
                    copia[i] = copia[i+1]
                    copia[i+1] = aux
    for cosa in contextoronda[contador]:
        if cosa == "ID_Ganador":
            contextoronda[contador][cosa] = copia[0]
    if contextoronda[contador][copia[0]]["Es_banca"]:
        for key in copia:
            if key not in copia[0]:
                if contextoronda[contador][copia[0]]["Apuesta"] > contextoronda[contador][key]["Apuesta"]:
                    contextoronda[contador][copia[0]]["Puntos"] += contextoronda[contador][key]["Apuesta"]
                    contextoronda[contador][key]["Puntos"] -=  contextoronda[contador][key]["Apuesta"]
                else:
                    contextoronda[contador][copia[0]]["Puntos"] += contextoronda[contador][copia[0]]["Apuesta"]
                    contextoronda[contador][key]["Puntos"] -= contextoronda[contador][copia[0]]["Apuesta"]
    else:
        for key in copia:
            if contextoronda[contador][key]["Es_banca"]:
                if contextoronda[contador][copia[0]]["Apuesta"] > contextoronda[contador][key]["Apuesta"]:
                    contextoronda[contador][copia[0]]["Puntos"] += contextoronda[contador][key]["Apuesta"]
                    contextoronda[contador][key]["Puntos"] -= contextoronda[contador][key]["Apuesta"]
                else:
                    contextoronda[contador][copia[0]]["Puntos"] += contextoronda[contador][copia[0]]["Apuesta"]
                    contextoronda[contador][key]["Puntos"] -= contextoronda[contador][copia[0]]["Apuesta"]
    if len(proxima_banca) > 0:
        for pasadas in range(len(proxima_banca)-1):
            for i in range(len(proxima_banca)-1-pasadas):
                if contextopartida[proxima_banca[i]]["Prioridad"] < contextopartida[proxima_banca[i+1]]["Prioridad"]:
                    aux = proxima_banca[i]
                    proxima_banca[i] = proxima_banca[i+1]
                    proxima_banca[i+1] = aux
    return proxima_banca

def decidir_jugada_bot(jugadores,turno,contador,players,ronda,partida,mazo,cartas):

    while True:
        aux = "Round: {} {}".format(contador, players[jugadores[turno - 1]]["Name"])

        print(aux.center(50, "="))
        print("Estado de jugadores".center(50, "="))
        print()
        print("Nombre".ljust(15) + "Humano".ljust(10) + "Prioridad".ljust(10) + "Tipo".ljust(10) +
              "Banca".ljust(10) + "Apuesta".ljust(10) + "Puntos".ljust(10) +
              "Cartas".ljust(15) + "Puntos ronda".ljust(15))
        print("=" * 120)

        for key in jugadores:
            print(players[key]["Name"].ljust(15) +
                str(players[key]["Type"]).ljust(13) +
                str(partida[key]["Prioridad"]).ljust(8) +
                str(players[key]["Risk"]).ljust(10) +
                str(ronda[contador][key]["Es_banca"]).ljust(10) +
                str(ronda[contador][key]["Apuesta"]).ljust(10) +
                str(ronda[contador][key]["Puntos"]).ljust(10) +
                str(ronda[contador][key]["Cartas"]).ljust(20) +
                str(ronda[contador][key]["Valor_total_cartas"]).ljust(15))

        input("\n\nPresiona enter para continuar".center(50,"-"))

        ronda[contador][jugadores[turno-1]]["Apuesta"] = random.randint(1, ronda[contador][jugadores[turno-1]]["Puntos"]//3)


        asignadas = []
        jugador_actual = jugadores[turno - 1]
        riesgo = players[jugador_actual]["Risk"]
        valor_actual = ronda[contador][jugador_actual]["Valor_total_cartas"]
        umbral_bueno = 7.5 - valor_actual
        terminar = False
        cartas_buenas = 0
        umbral_probabilidad = 0

        for key in jugadores:
            for i in range(len(ronda[contador][key]["Cartas"])):
                asignadas.append(ronda[contador][key]["Cartas"][i])

        for carta in mazo:
            if carta not in asignadas and cartas[carta]["value"] <= umbral_bueno:
                cartas_buenas += 1

        total_cartas_disponibles = 52 - len(asignadas)
        probabilidad_buena = cartas_buenas / total_cartas_disponibles

        if riesgo == 1:
            umbral_probabilidad = 0.7
        elif riesgo == 2:
            umbral_probabilidad = 0.6
        elif riesgo == 3:
            umbral_probabilidad = 0.5

        if probabilidad_buena >= umbral_probabilidad:

            loginfo(f"{players[jugador_actual]['Name']} decide pedir una carta.")

            while not terminar:
                carta = mazo[random.randint(0, len(mazo) - 1)]
                if carta not in asignadas:
                    ronda[contador][jugador_actual]["Cartas"].append(carta)
                    ronda[contador][jugador_actual]["Valor_total_cartas"] += cartas[carta]["value"]
                    terminar = True

        else:
            loginfo(f"{players[jugador_actual]['Name']} decide plantarse.")
            # El bot decide no pedir mÃ¡s cartas
            return

def decidir_jugada_banca(jugadores,turno,contador,players,ronda,partida,mazo,cartas):

    while True:
        aux = "Round: {} {}".format(contador, players[jugadores[turno - 1]]["Name"])

        print(aux.center(50, "="))
        print("Estado de jugadores".center(50, "="))
        print()
        print("Nombre".ljust(15) + "Humano".ljust(10) + "Prioridad".ljust(10) + "Tipo".ljust(10) +
              "Banca".ljust(10) + "Apuesta".ljust(10) + "Puntos".ljust(10) +
              "Cartas".ljust(15) + "Puntos ronda".ljust(15))
        print("=" * 120)

        for key in jugadores:
            print(players[key]["Name"].ljust(15) +
                str(players[key]["Type"]).ljust(13) +
                str(partida[key]["Prioridad"]).ljust(8) +
                str(players[key]["Risk"]).ljust(10) +
                str(ronda[contador][key]["Es_banca"]).ljust(10) +
                str(ronda[contador][key]["Apuesta"]).ljust(10) +
                str(ronda[contador][key]["Puntos"]).ljust(10) +
                str(ronda[contador][key]["Cartas"]).ljust(20) +
                str(ronda[contador][key]["Valor_total_cartas"]).ljust(15))

        input("\n\nPresiona enter para continuar".center(50,"-"))

        ronda[contador][jugadores[turno-1]]["Apuesta"] = random.randint(1, ronda[contador][jugadores[turno-1]]["Puntos"]//3)


        asignadas = []
        jugador_actual = jugadores[turno - 1]
        riesgo = players[jugador_actual]["Risk"]
        valor_actual = ronda[contador][jugador_actual]["Valor_total_cartas"]
        umbral_bueno = 7.5 - valor_actual
        terminar = False
        cartas_buenas = 0
        umbral_probabilidad = 0

        for key in jugadores:
            for i in range(len(ronda[contador][key]["Cartas"])):
                asignadas.append(ronda[contador][key]["Cartas"][i])

        for carta in mazo:
            if carta not in asignadas and cartas[carta]["value"] <= umbral_bueno:
                cartas_buenas += 1

        total_cartas_disponibles = 52 - len(asignadas)
        probabilidad_buena = cartas_buenas / total_cartas_disponibles

        if riesgo == 1:
            umbral_probabilidad = 0.7
        elif riesgo == 2:
            umbral_probabilidad = 0.6
        elif riesgo == 3:
            umbral_probabilidad = 0.5

        for jugador in jugadores:
            if ronda[contador][jugador]["Valor_total_cartas"] > umbral_bueno and ronda[contador][jugador]["Valor_total_cartas"] <= 7.5:

                if probabilidad_buena >= 0.65:

                    loginfo(f"{players[jugador_actual]['Name']} decide pedir una carta.")

                    while not terminar:
                        carta = mazo[random.randint(0, len(mazo) - 1)]
                        if carta not in asignadas:
                            ronda[contador][jugador_actual]["Cartas"].append(carta)
                            ronda[contador][jugador_actual]["Valor_total_cartas"] += cartas[carta]["value"]
                            terminar = True
                            continue

        if probabilidad_buena >= umbral_probabilidad:

            loginfo(f"{players[jugador_actual]['Name']} decide pedir una carta.")

            while not terminar:
                carta = mazo[random.randint(0, len(mazo) - 1)]
                if carta not in asignadas:
                    ronda[contador][jugador_actual]["Cartas"].append(carta)
                    ronda[contador][jugador_actual]["Valor_total_cartas"] += cartas[carta]["value"]
                    terminar = True

        else:
            loginfo(f"{players[jugador_actual]['Name']} decide plantarse.")
            # El bot decide no pedir mÃ¡s cartas
            return

def elegirganador(nueva_partida,jugadores,players):
    print()
    comparar = []
    for key in jugadores:
        comparar.append(nueva_partida[key]["Puntos_finales"]-nueva_partida[key]["Puntos_iniciales"])
    for pasadas in range(len(comparar)-1):
        for i in range(len(comparar)-1-pasadas):
            if comparar[i] < comparar[i+1]:
                aux = comparar[i]
                comparar[i] = comparar[i+1]
                comparar[i+1] = aux
    for jugador in jugadores:
        if nueva_partida[jugador]["Puntos_finales"]-nueva_partida[jugador]["Puntos_iniciales"] == comparar[0]:
            print("¡Felicidades has ganado {}!".format(players[jugador]["Name"]))
            return jugador
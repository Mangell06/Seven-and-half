import datetime

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
        input("Press enter to continue".center(50))

#Imprimir stats de bots y jugadores por separado.
def printStats(players):
    jugador_prio_mas_alta = None
    for player in players:
        if jugador_prio_mas_alta is None or player['Priority'] > jugador_prio_mas_alta['Priority']:
            jugador_prio_mas_alta = player
    print(15*"*"+ "Round 0 , Turn of {}" +15*"*".format(jugador_prio_mas_alta['Name']))
    print("{:<10} {:<9} {:<9} {:<4} {:<4} {:<5} {:<6} {:<11} {:<12}".format(
        "Name", "Human", "Priority", "Type", "Bank", "Bet", "Points", "Cards", "Roundpoints"))
    for player in players:
        print("{:<10} {:<9} {:<9} {:<4} {:<4} {:<5} {:<6} {:<11} {:.1f}".format(
            player['Name'],
            player['Human'],
            player['Priority'],
            player['Type'],
            player['Bank'],
            player['Bet'],
            player['Points'],
            player['Cards'],
            player['Roundpoints']
        ))

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
        input("Press enter to continue".center(50))

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

def raking_minuts_played():
    personajes_dict = {
        "1234": {"Name": "Juan", "Risk": "Moderado", "Type": "Bot", "Puntos": 50, "Minutos_Jugados": 100},
        "5678": {"Name": "Ana", "Risk": "Miedoso", "Type": "Human", "Puntos": 75, "Minutos_Jugados": 200},
        "2345": {"Name": "Luis", "Risk": "Audaz", "Type": "Bot", "Puntos": 65, "Minutos_Jugados": 150},
        "6789": {"Name": "Isabel", "Risk": "Moderado", "Type": "Human", "Puntos": 80, "Minutos_Jugados": 180},
        "3456": {"Name": "Carlos", "Risk": "Miedoso", "Type": "Bot", "Puntos": 55, "Minutos_Jugados": 120},
        "7890": {"Name": "María", "Risk": "Audaz", "Type": "Human", "Puntos": 70, "Minutos_Jugados": 170},
        "4567": {"Name": "Andrea", "Risk": "Moderado", "Type": "Human", "Puntos": 85, "Minutos_Jugados": 210},
        "8901": {"Name": "Pedro", "Risk": "Miedoso", "Type": "Bot", "Puntos": 60, "Minutos_Jugados": 140},
        "5679": {"Name": "Lucía", "Risk": "Audaz", "Type": "Human", "Puntos": 90, "Minutos_Jugados": 220},
        "9012": {"Name": "Miguel", "Risk": "Moderado", "Type": "Bot", "Puntos": 75, "Minutos_Jugados": 130},
        "6780": {"Name": "Clara", "Risk": "Miedoso", "Type": "Human", "Puntos": 95, "Minutos_Jugados": 230},
        "1235": {"Name": "David", "Risk": "Audaz", "Type": "Bot", "Puntos": 50, "Minutos_Jugados": 110},
    }

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
            print(str(ID).ljust(10) + personaje["Name"].ljust(15) + personaje["Risk"].ljust(10) + personaje["Type"].ljust(12) + str(personaje["Puntos"]).rjust(10) + str(personaje["Minutos_Jugados"]).rjust(18))

        elegir = input("Avanza (+) o retrocede (-), y 0 para salir: ".rjust(30))
        if elegir == "+":
            if (pag + 1) * 10 < len(lista_ordenar):
                pag += 1
        elif elegir == "-":
            if pag > 0:
                pag -= 1
        elif elegir == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def raking_id():
    personajes_dict = {
        "1234": {"Name": "Juan", "Risk": "Moderado", "Type": "Bot", "Puntos": 50, "Minutos_Jugados": 100},
        "5678": {"Name": "Ana", "Risk": "Miedoso", "Type": "Human", "Puntos": 75, "Minutos_Jugados": 200},
        "2345": {"Name": "Luis", "Risk": "Audaz", "Type": "Bot", "Puntos": 65, "Minutos_Jugados": 150},
        "6789": {"Name": "Isabel", "Risk": "Moderado", "Type": "Human", "Puntos": 80, "Minutos_Jugados": 180},
        "3456": {"Name": "Carlos", "Risk": "Miedoso", "Type": "Bot", "Puntos": 55, "Minutos_Jugados": 120},
        "7890": {"Name": "María", "Risk": "Audaz", "Type": "Human", "Puntos": 70, "Minutos_Jugados": 170},
        "4567": {"Name": "Andrea", "Risk": "Moderado", "Type": "Human", "Puntos": 85, "Minutos_Jugados": 210},
        "8901": {"Name": "Pedro", "Risk": "Miedoso", "Type": "Bot", "Puntos": 60, "Minutos_Jugados": 140},
        "5679": {"Name": "Lucía", "Risk": "Audaz", "Type": "Human", "Puntos": 90, "Minutos_Jugados": 220},
        "9012": {"Name": "Miguel", "Risk": "Moderado", "Type": "Bot", "Puntos": 75, "Minutos_Jugados": 130},
        "6780": {"Name": "Clara", "Risk": "Miedoso", "Type": "Human", "Puntos": 95, "Minutos_Jugados": 230},
        "1235": {"Name": "David", "Risk": "Audaz", "Type": "Bot", "Puntos": 50, "Minutos_Jugados": 110},
    }

    lista_ordenar = list(personajes_dict.keys())

    for pasadas in range(len(lista_ordenar)):
        cambios = False
        for i in range(len(lista_ordenar) - 1 - pasadas):
            if int(lista_ordenar[i]) > int(lista_ordenar[i + 1]):
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
            print(str(ID).ljust(10) + personaje["Name"].ljust(15) + personaje["Risk"].ljust(10) + personaje["Type"].ljust(12) + str(personaje["Puntos"]).rjust(10) + str(personaje["Minutos_Jugados"]).rjust(18))

        elegir = input("Avanza (+) o retrocede (-), y 0 para salir: ".rjust(30))
        if elegir == "+":
            if (pag + 1) * 10 < len(lista_ordenar):
                pag += 1
        elif elegir == "-":
            if pag > 0:
                pag -= 1
        elif elegir == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def raking_puntos():
    personajes_dict = {
        "1234": {"Name": "Juan", "Risk": "Moderado", "Type": "Bot", "Puntos": 50, "Minutos_Jugados": 100},
        "5678": {"Name": "Ana", "Risk": "Miedoso", "Type": "Human", "Puntos": 75, "Minutos_Jugados": 200},
        "2345": {"Name": "Luis", "Risk": "Audaz", "Type": "Bot", "Puntos": 65, "Minutos_Jugados": 150},
        "6789": {"Name": "Isabel", "Risk": "Moderado", "Type": "Human", "Puntos": 80, "Minutos_Jugados": 180},
        "3456": {"Name": "Carlos", "Risk": "Miedoso", "Type": "Bot", "Puntos": 55, "Minutos_Jugados": 120},
        "7890": {"Name": "María", "Risk": "Audaz", "Type": "Human", "Puntos": 70, "Minutos_Jugados": 170},
        "4567": {"Name": "Andrea", "Risk": "Moderado", "Type": "Human", "Puntos": 85, "Minutos_Jugados": 210},
        "8901": {"Name": "Pedro", "Risk": "Miedoso", "Type": "Bot", "Puntos": 60, "Minutos_Jugados": 140},
        "5679": {"Name": "Lucía", "Risk": "Audaz", "Type": "Human", "Puntos": 90, "Minutos_Jugados": 220},
        "9012": {"Name": "Miguel", "Risk": "Moderado", "Type": "Bot", "Puntos": 75, "Minutos_Jugados": 130},
        "6780": {"Name": "Clara", "Risk": "Miedoso", "Type": "Human", "Puntos": 95, "Minutos_Jugados": 230},
        "1235": {"Name": "David", "Risk": "Audaz", "Type": "Bot", "Puntos": 50, "Minutos_Jugados": 110},
    }

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
            print(str(ID).ljust(10) + personaje["Name"].ljust(15) + personaje["Risk"].ljust(10) + personaje["Type"].ljust(12) + str(personaje["Puntos"]).rjust(10) + str(personaje["Minutos_Jugados"]).rjust(18))

        elegir = input("Avanza (+) o retrocede (-), y 0 para salir: ".rjust(30))
        if elegir == "+":
            if (pag + 1) * 10 < len(lista_ordenar):
                pag += 1
        elif elegir == "-":
            if pag > 0:
                pag -= 1
        elif elegir == "0":
            break
        else:
            print("Opción inválida. Intente de nuevo.")
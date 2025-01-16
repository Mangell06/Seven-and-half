import FUCTIONS.MANAGEMENT as manage

def setPlayersGame(players_dict):
    players_game = []
    while True:
        num_players = input("Ingrese el número de jugadores para la partida: ")
        if not num_players.isdigit():
            print("Error: opción no numérica. Inténtalo de nuevo.")
            continue
        num_players = int(num_players)
        if num_players <= 0 or num_players > len(players_dict):
            print("Error: el número de jugadores debe ser mayor que cero y menor o igual que {}. Inténtalo de nuevo.".format(len(players_dict)))
            continue
        break

    available_players = list(players_dict.keys())
    print("Lista de jugadores disponibles:")
    idx = 1
    for player_id in available_players:
        player = players_dict[player_id]
        print("{}: {} (ID: {})".format(idx, player['Name'], player_id))
        idx += 1

    for i in range(num_players):
        while True:
            idx_selected = int(input("Seleccione el número del jugador {} para la partida: ".format(i + 1))) - 1
            if 0 <= idx_selected < len(available_players):
                player_id = available_players[idx_selected]
                player_already_selected = False
                for p in players_game:
                    if p['ID'] == player_id:
                        player_already_selected = True
                        break
                if not player_already_selected:
                    players_game.append(players_dict[player_id])
                    print("Jugador {} añadido. Jugadores actuales en la partida:".format(players_dict[player_id]['Name']))
                    print(10*"*"+"Actual Player in Game"+10*"*")
                    for p in players_game:
                        print("{} (ID: {})".format(p['Name'], p['ID']))
                    break
                else:
                    print("Jugador ya seleccionado. Por favor, elija otro.")
            else:
                print("Número de jugador inválido. Inténtalo de nuevo.")

    return players_game

def printStats(players={}):

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
            manage.loginfo("Se a creado un nuevo ID")
            return dni.upper()
        print()
        input("Press enter to continue".center(50))
import FUCTIONS.MANAGEMENT as manage

#  personajes_dict = {row['ID']: {"Name": row['Name'], "Risk": row['Risk'],
#  "Type": row["Type"], "Puntos": row["Puntos"], "Minutos_Jugados": row["Minutos_Jugados"],
#  "In_Game": row["In_Game"]}

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
    for idx, player_id in enumerate(available_players, start=1):
        player = players_dict[player_id]
        print("{}: {} (ID: {})".format(idx, player['Name'], player_id))

    for i in range(num_players):
        while True:
            idx_selected = int(input("Seleccione el número del jugador {} para la partida: ".format(i + 1))) - 1
            if 0 <= idx_selected < len(available_players):
                player_id = available_players[idx_selected]
                if player_id not in [p['ID'] for p in players_game]:
                    player = players_dict[player_id]
                    players_game.append({'ID': player_id, 'Name': player['Name']})
                    print("Jugador '{}' añadido. Jugadores actuales en la partida:".format(player['Name']))
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

def newPlayer(dni):
    player_info = {
        'name': "Hola",
        'human': False,
        'bank': 0,
        'initialCard': "",
        'priority': 0,
        'type': '',
        'bet': 0,
        'points': 0,
        'cards': [],
        'roundPoints': 0
    }
    return dni, player_info
dni = '12345678A'
new_player = newPlayer(dni)
print(new_player)

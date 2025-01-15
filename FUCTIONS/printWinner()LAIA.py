def printWinner(players):
    """
    Muestra el ganador de la partida.
    :param players: Lista de diccionarios con información de los jugadores.
                    Cada diccionario debe contener las claves 'name' y 'score'.
    :return: None
    """
    if not players:
        print("No hay jugadores en la partida.")
        return

    # Encontrar el jugador con la mayor puntuación
    winner = max(players, key=lambda player: player['score'])

    # Verificar si hay empate
    highest_score = winner['score']
    tied_players = [player for player in players if player['score'] == highest_score]

    if len(tied_players) > 1:
        print("Hay un empate entre los siguientes jugadores:")
        for player in tied_players:
            print(f"- {player['name']} con {player['score']} puntos")
    else:
        print(f"El ganador es {winner['name']} con {winner['score']} puntos. ¡Felicidades!")

# Ejemplo de uso
if __name__ == "__main__":
    jugadores = [
        {"name": "Laia", "score": 150},
        {"name": "Alex", "score": 200},
        {"name": "Maria", "score": 200}
    ]

    printWinner(jugadores)

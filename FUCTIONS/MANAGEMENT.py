def loginfo(texto):
    f = open("Seven_and_Half_LOG.txt", "a")
    f.write(texto)
    f.close()

def management_menu(title=1,menu=()):
    while True:
        if title >= 1:
            print("".center(50,"="))
            for i in range(title):
                print(menu[i].center(50))
            print("".center(50,"="))
        for i in range(title,len(menu)):
            aux = str(i-title//2) + ") " + menu[i]
            print(aux.center(50))
        option = input("Option: ".rjust(29))
        print()
        if not option.isdigit():
            print("Invalid Option".center(50,"="))
        elif int(option) not in range(1,len(menu)-title//2):
            print("Invalid Option".center(50,"="))
        else:
            loginfo("\nEl jugador a elegido una opcion")
            return int(option)
        print()
        input("Press enter to continue")

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
            loginfo("\nSe a creado un nuevo ID")
            return dni.upper()
        print()
        input("Press enter to continue".center(50))


""" FUNCIÓN DE IMPRIMIR EL GANADOR - LAIA """
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



    """ FUNCIÓN PARA ELIMINAR UN JUGADOR DE LA BASE DE DATOS USANDO SU NIF- LAIA """
    import sqlite3


    def delBBDDPlayer(nif):
        try:
            # Conexión a la base de datos (reemplazar 'mi_base_de_datos.db' con el nombre real)
            conexion = sqlite3.connect('mi_base_de_datos.db')
            cursor = conexion.cursor()

            # Consulta para eliminar el jugador por su NIF
            consulta = "DELETE FROM jugadores WHERE nif = ?"

            # Ejecutar la consulta
            cursor.execute(consulta, (nif,))
            conexion.commit()  # Guardar los cambios

            if cursor.rowcount > 0:
                print(f"El jugador con NIF {nif} ha sido eliminado.")
            else:
                print(f"No se encontró ningún jugador con el NIF {nif}.")

        except sqlite3.Error as e:
            print(f"Error al eliminar el jugador: {e}")

        finally:
            # Cerrar la conexión
            if conexion:
                conexion.close()
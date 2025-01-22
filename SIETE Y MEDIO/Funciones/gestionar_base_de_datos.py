import gestionar_juego as juego
import pymysql

# Configuración de conexión
db_config = {
    'host': 'server-proyecto-2025.mysql.database.azure.com',
    'user': 'Proyecto',
    'password': 'Huevo19421942',
    'database': 'siete_y_medio',
    'port': 3306
}

def connect_to_database():
    """Establece una conexión con la base de datos MySQL."""
    try:
        # Crear la conexión
        connection = pymysql.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database'],
            port=db_config['port']
        )
        juego.loginfo("Conexión exitosa a la base de datos.")
        return connection
    except pymysql.MySQLError as e:
        juego.loginfo(f"Error al conectar a la base de datos: {e}")
        return None

def close_connection(connection):
    """Cierra la conexión con la base de datos."""
    if connection:
        connection.close()
        juego.loginfo("Conexión cerrada.")

def delBBDDPlayer(nif):
    """
    Elimina un jugador de la base de datos con el NIF proporcionado.
    """
    query = "DELETE FROM personajes WHERE ID = %s;"  # Consulta para eliminar al jugador
    connection = connect_to_database()  # Conecta a la base de datos

    if not connection:
        juego.loginfo("Error: No se pudo conectar a la base de datos.")
        return

    try:
        with connection.cursor() as cursor:  # Crear un cursor para ejecutar la consulta
            cursor.execute(query, (nif,))  # Ejecutar la consulta con el NIF como parámetro
            connection.commit()  # Confirmar los cambios

            # Verificar si se eliminó alguna fila
            if cursor.rowcount > 0:
                juego.loginfo(f"El jugador con NIF {nif} ha sido eliminado.")
            else:
                juego.loginfo(f"No se encontró ningún jugador con el NIF {nif}.")
    except pymysql.MySQLError as e:
        juego.loginfo(f"Error al eliminar el jugador: {e}")
    finally:
        close_connection(connection)  # Cerrar la conexión

def execute_query(connection, query):
    """Ejecuta una consulta SQL y devuelve los resultados."""
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:  # Usar DictCursor
            cursor.execute(query)
            results = cursor.fetchall()
            return results
    except pymysql.MySQLError as e:
        juego.loginfo(f"Error al ejecutar la consulta: {e}")
        return None

def get_cartas():
    """Consulta la tabla de Cartas y devuelve los resultados como un diccionario."""
    query = "SELECT * FROM siete_y_medio.cartas;"  # Consulta a la tabla Cartas
    connection = connect_to_database()

    if connection:
        results = execute_query(connection, query)
        close_connection(connection)
        if results:
            # Diccionario con ID_Jugadores como clave
            cartas_dict = {
                row['ID_Jugadores']: {
                    "Carta_Inicial_Mas_Repetida": row['Carta_Inicial_Mas_Repetida'],
                    "Carta_Inicial_Mas_Repetida_XVeces": row['Carta_inicial_Mas_Repetida_XVeces'],
                    "Carta_Inicial_Mas_Repetida_Palo": row['Carta_inicial_Mas_Repetida_Palo'],
                    "Carta_Inicial_Mas_Repetida_Palo_XVeces": row['Carta_inicial_Mas_Repetida_Palo_XVeces'],
                } for row in results
            }
            return cartas_dict
    return {}


def get_partidas():
    """Consulta la tabla de Partidas y devuelve los resultados como un diccionario."""
    query = "SELECT * FROM siete_y_medio.partidas;"  # Consulta a la tabla Partidas
    connection = connect_to_database()

    if connection:
        results = execute_query(connection, query)
        close_connection(connection)
        if results:
            # Diccionario con ID_Partida como clave
            partidas_dict = {
                row['ID_Partida']: {
                    "Fecha": row['Fecha'],
                    "ID_Ganador": row['ID_Ganador'],
                    "Total_Rondas": row['Total_Rondas'],
                    "Mazo": row['Mazo'],
                } for row in results
            }
            return partidas_dict
    return {}


def get_personajes():
    """Consulta la tabla de Personajes y devuelve los resultados como un diccionario."""
    query = "SELECT * FROM personajes;"  # Consulta a la tabla Personajes
    connection = connect_to_database()

    if connection:
        results = execute_query(connection, query)
        close_connection(connection)  # Asegúrate de cerrar la conexión después de la consulta
        if results:
            # Crear un diccionario usando 'ID' como clave
            personajes_dict = {
                row['ID']: {
                    "Name": row['Name'],
                    "Risk": row['Risk'],
                    "Type": row["Type"],
                    "Puntos": row["Puntos"],
                    "Minutos_Jugados": row["Minutos_Jugados"],
                    "In_Game": None if row["In_Game"] is None else bool(row["In_Game"])  # Convertir a True, False o None
                }
                for row in results
            }
            return personajes_dict  # Devuelve el diccionario
    return {}  # Devuelve un diccionario vacío si no hay resultados o hay un error


def actualizar_in_game(dni_list, in_game_value):
    """
    Actualiza el valor de In_Game para los jugadores con los DNIs proporcionados.

    :param dni_list: Lista de DNIs de los jugadores a actualizar.
    :param in_game_value: Valor a establecer en el campo In_Game (True o False).
    """
    # Convertir el valor booleano a un entero (MySQL espera 0 o 1)
    in_game_value = 1 if in_game_value else 0

    # Establecer la conexión
    connection = connect_to_database()
    if not connection:
        return

    try:
        # Construir la consulta SQL
        query = "UPDATE personajes SET In_Game = %s WHERE ID = %s"

        # Crear un cursor
        with connection.cursor() as cursor:
            # Actualizar cada jugador de la lista
            for dni in dni_list:
                cursor.execute(query, (in_game_value, dni))

        # Confirmar los cambios
        connection.commit()
        juego.loginfo(f"In_Game actualizado a {in_game_value} para los DNIs: {dni_list}")

    except pymysql.MySQLError as e:
        juego.loginfo(f"Error al actualizar jugadores: {e}")

    finally:
        # Cerrar la conexión
        close_connection(connection)


def activar_jugadores(dni_list):
    """
    Activa a los jugadores estableciendo In_Game a True para los DNIs proporcionados.

    :param dni_list: Lista de DNIs de los jugadores a activar.
    """
    actualizar_in_game(dni_list, True)


def desactivar_jugadores(dni_list):
    """
    Desactiva a los jugadores estableciendo In_Game a False para los DNIs proporcionados.

    :param dni_list: Lista de DNIs de los jugadores a desactivar.
    """
    actualizar_in_game(dni_list, False)


def insertar_personaje_base_datos(player_data):
    """
    Inserta un nuevo personaje en la base de datos.

    :param player_data: Diccionario con los datos del personaje.
    """
    connection = connect_to_database()
    if not connection:
        return

    try:
        # Construir la consulta de inserción
        query = """
            INSERT INTO personajes (ID, Name, Risk, Type, Puntos, Minutos_Jugados, In_Game)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        # Ejecutar la consulta
        with connection.cursor() as cursor:
            cursor.execute(query, (
                player_data["ID"],
                player_data["Name"],
                player_data["Risk"],
                player_data["Type"],
                player_data["Puntos"],
                player_data["Minutos_Jugados"],
                int(player_data["In_Game"])  # Convertir booleano a entero (1 o 0)
            ))
        connection.commit()
        juego.loginfo(f"Personaje {player_data['Name']} añadido a la base de datos correctamente.")
    except pymysql.MySQLError as e:
        juego.loginfo(f"Error al insertar el personaje en la base de datos: {e}")
    finally:
        close_connection(connection)


def insertar_rondas(player_round, new_party, partidas_dicti, player_party):
    """
    Inserta los datos de las rondas en la base de datos.

    Args:
        player_round (dict): Diccionario con la información de cada ronda.
        new_party (dict): Diccionario con la información de la partida actual.
        partidas_dicti (dict): Diccionario con el historial de partidas.
        player_party (dict): Diccionario con los datos iniciales y finales de cada jugador.
    """
    connection = connect_to_database()
    try:
        with connection.cursor() as cursor:
            # Obtener ID_Partida
            id_partida = len(partidas_dicti) + 1

            # Obtener Rondas_Max
            rondas_max = new_party["Total_Rondas"]

            # Crear un diccionario para almacenar los puntos finales por jugador por ronda
            puntos_finales_por_jugador = {}

            # Insertar datos de cada ronda
            for id_ronda, ronda_data in player_round.items():
                id_ganador = ronda_data["ID_Ganador"] if "ID_Ganador" in ronda_data else None

                # Iterar por cada jugador en la ronda
                for id_jugador, jugador_data in ronda_data.items():
                    if id_jugador == "ID_Ganador":
                        continue  # Saltar el campo de ganador

                    # Verificar que el jugador está en player_party para evitar errores
                    if id_jugador in player_party:
                        # Obtener puntos iniciales o usar puntos finales de la ronda anterior
                        if id_ronda == 0:
                            puntos_iniciales = player_party[id_jugador]["Puntos_iniciales"]
                        else:
                            puntos_iniciales = puntos_finales_por_jugador.get(id_jugador, 0)

                        # Obtener puntos finales de la ronda actual
                        puntos_finales = jugador_data["Puntos"]

                        # Calcular los puntos ganados
                        puntos_ganados = puntos_finales - puntos_iniciales

                        # Almacenar los puntos finales para la próxima ronda
                        puntos_finales_por_jugador[id_jugador] = puntos_finales

                        # Obtener datos de la ronda
                        apuesta = jugador_data["Apuesta"]
                        banca = int(jugador_data["Es_banca"])  # Convertir a 1 o 0

                        # Query de inserción
                        query = """
                            INSERT INTO rondas (ID_Ronda, ID_Partida, Rondas_Max, ID_Jugador, 
                                                Puntos_Ganados, Apuesta, Banca)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """
                        cursor.execute(query, (id_ronda, id_partida, rondas_max, id_jugador,
                                               puntos_ganados, apuesta, banca))

            # Confirmar cambios
            connection.commit()
            juego.loginfo(f"Datos de rondas insertados correctamente para ID_Partida {id_partida}.")
    except pymysql.MySQLError as e:
        juego.loginfo(f"Error al insertar los datos de rondas: {e}")
        connection.rollback()
    finally:
        close_connection(connection)

def insertar_historial(player_party, partidas_dicti, tiempo_jugado):
    """
    Inserta los datos en la tabla 'historial' de la base de datos.

    Args:
        player_party (dict): Diccionario con información de los jugadores en la partida.
        partidas_dicti (dict): Diccionario con las partidas y su información.
    """
    connection = connect_to_database()
    try:
        with connection.cursor() as cursor:
            # Obtener ID_Partida (basado en el tamaño del diccionario de partidas)
            id_partida = len(partidas_dicti) + 1

            # Insertar los datos de cada jugador en la partida
            for id_jugador, datos_jugador in player_party.items():
                # Obtener los valores necesarios
                puntos_iniciales = datos_jugador["Puntos_iniciales"]
                puntos_finales = datos_jugador["Puntos_finales"]
                Tiempo_Jugado = tiempo_jugado

                # Query de inserción en la tabla historial
                query = """
                    INSERT INTO historial (ID_Jugador, ID_Partida, Puntos_Iniciales, Puntos_Finales, Tiempo_Jugado)
                    VALUES (%s, %s, %s, %s, %s)
                """
                # Ejecutar el query
                cursor.execute(query, (id_jugador, id_partida, puntos_iniciales, puntos_finales, Tiempo_Jugado))

            # Confirmar los cambios
            connection.commit()
            juego.loginfo(f"Datos de historial insertados correctamente para ID_Partida {id_partida}.")
    except pymysql.MySQLError as e:
        juego.loginfo(f"Error al insertar los datos en historial: {e}")
        connection.rollback()
    finally:
        close_connection(connection)

def insertar_partidas(partidas_dicti, new_party,id_ganador):
    """
    Inserta los datos de la partida en la tabla 'partidas' de la base de datos.

    Args:
        partidas_dicti (dict): Diccionario con la información de las partidas.
        new_party (dict): Diccionario con los datos de la nueva partida.
    """
    connection = connect_to_database()
    try:
        with connection.cursor() as cursor:
            # Obtener ID_Partida (basado en el tamaño del diccionario de partidas)
            id_partida = len(partidas_dicti) + 1

            # Obtener información de la nueva partida
            fecha = new_party["start_date"]
            ID_ganador = id_ganador
            total_rondas = new_party["Total_Rondas"]
            mazo = new_party["Mazo"]

            # Query de inserción en la tabla partidas
            query = """
                INSERT INTO partidas (ID_Partida, Fecha, ID_Ganador, Total_Rondas, Mazo)
                VALUES (%s, %s, %s, %s, %s)
            """
            # Ejecutar el query
            cursor.execute(query, (id_partida, fecha, ID_ganador, total_rondas, mazo))

            # Confirmar los cambios
            connection.commit()
            juego.loginfo(f"Datos de partida insertados correctamente para ID_Partida {id_partida}.")
    except pymysql.MySQLError as e:
        juego.loginfo(f"Error al insertar los datos de la partida: {e}")
        connection.rollback()
    finally:
        close_connection(connection)


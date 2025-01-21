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


def get_historial():
    """Consulta la tabla de Historial y devuelve los resultados como un diccionario."""
    query = "SELECT * FROM siete_y_medio.historial;"  # Consulta a la tabla Historial
    connection = connect_to_database()

    if connection:
        results = execute_query(connection, query)
        close_connection(connection)
        if results:
            # Diccionario con ID_Jugador como clave
            historial_dict = {
                row['ID_Jugador']: {
                    "ID_Partida": row['ID_Partida'],
                    "Puntos_Iniciales": row['Puntos_Iniciales'],
                    "Puntos_Finales": row['Puntos_Finales'],
                    "Tiempo_Jugado": row['Tiempo_Jugado'],
                } for row in results
            }
            return historial_dict
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
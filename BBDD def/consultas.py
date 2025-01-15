import pymysql
from conexion import connect_to_database, close_connection

def execute_query(connection, query):
    """Ejecuta una consulta SQL y devuelve los resultados."""
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:  # Usar DictCursor
            cursor.execute(query)
            results = cursor.fetchall()
            return results
    except pymysql.MySQLError as e:
        print(f"Error al ejecutar la consulta: {e}")
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
                    "Carta_Inicial_Mas_Repetida_XVeces": row['Carta_Inicial_Mas_Repetida_XVeces'],
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
            # Crear un diccionario usando 'id' como clave
            personajes_dict = {row['ID']: {"Name": row['Name'], "Risk": row['Risk'], "Type": row["Type"], "Puntos": row["Puntos"], "Minutos_Jugados": row["Minutos_Jugados"], "In_Game": row["In_Game"]} for row in results}
            return personajes_dict  # Devuelve el diccionario
    return {}  # Devuelve un diccionario vacío si no hay resultados o hay un error


# Guardar los resultados en un diccionario
personajes_dict = get_personajes()

historial_dict = get_historial()

# Usar la variable 'personajes_dict' para lo que necesites
print(personajes_dict)  # Muestra el diccionario

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

# Usar la variable 'personajes_dict' para lo que necesites
print(personajes_dict)  # Muestra el diccionario

import pymysql

from conexion import connect_to_database, close_connection

def execute_query(connection, query):
    """Ejecuta una consulta SQL y devuelve los resultados."""
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
    except pymysql.MySQLError as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None


def get_personajes():
    """Consulta la tabla de Personajes y devuelve los resultados."""
    query = "SELECT * FROM personajes;"  # Consulta a la tabla Personajes
    connection = connect_to_database()

    if connection:
        results = execute_query(connection, query)
        if results:
            for row in results:
                print(row)  # Muestra cada fila (registro) en la tabla
        close_connection(connection)


if __name__ == "__main__":
    # Llamamos a la función que consulta los personajes
    get_personajes()


# Type = 1 = Cauteloso
# Type = 2 = Normal
# Type = 3 = Agresivo


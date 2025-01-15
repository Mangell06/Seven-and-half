import sqlite3
import pymysql
from FUCTIONS.MANAGEMENT import loginfo

db_config = {
    'host': 'server-proyecto-2025.mysql.database.azure.com',
    'user': 'Proyecto',
    'password': 'Huevo19421942',
    'database': 'siete_y_medio',
    'port': 3306
}

def delBBDDPlayer(nif):
    try:
        conexion = sqlite3.connect('mi_base_de_datos.db')
        cursor = conexion.cursor()
        consulta = "DELETE FROM jugadores WHERE nif = ?"
        cursor.execute(consulta, (nif,))
        conexion.commit()
        if cursor.rowcount > 0:
            loginfo("\nEl jugador con NIF {} ha sido eliminado.".format(nif))
            print("El jugador a sido eliminado.")
        else:
            print("\nNo se encontró ningún jugador con el NIF {}.".format(nif))
    except sqlite3.Error as e:
        loginfo("\nError 101001: Error al eliminar el jugador: {}".format(e))
        print(f"Error 101001 revisa el archivo Seven_and_Half_LOG.txt para más información.")
    finally:
        if conexion:
            conexion.close()

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
        print("Conexión exitosa a la base de datos.")
        return connection
    except pymysql.MySQLError as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def close_connection(connection):
    """Cierra la conexión con la base de datos."""
    if connection:
        connection.close()
        print("Conexión cerrada.")
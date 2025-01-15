import sqlite3
from FUCTIONS.MANAGEMENT import loginfo


def delBBDDPlayer(nif):
    try:
        conexion = sqlite3.connect('mi_base_de_datos.db')
        cursor = conexion.cursor()
        consulta = "DELETE FROM jugadores WHERE nif = ?"
        cursor.execute(consulta, (nif,))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"El jugador con NIF {nif} ha sido eliminado.")
        else:
            print(f"No se encontró ningún jugador con el NIF {nif}.")
    except sqlite3.Error as e:
        loginfo(f"Error 101001: Error al eliminar el jugador: {e}")
        print(f"Error 101001 revisa el archivo Seven_and_Half_LOG.txt para más información.")
    finally:
        if conexion:
            conexion.close()
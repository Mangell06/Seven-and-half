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
import sqlite3

def delBBDDPlayer(nif):
    """
    Elimina un jugador de la base de datos usando su NIF.
    :param nif: Cadena que representa el NIF del jugador a eliminar.
    """
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

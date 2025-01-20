from gestionar_base_de_datos import connect_to_database, execute_query, close_connection, get_cartas
from gestionar_juego import loginfo

# ============================================================
# CONSULTAS A LA BASE DE DATOS
# ============================================================


def carta_inicial_mas_repetida_con_get_cartas():
    """
    Obtiene la carta inicial más repetida por cada jugador que haya jugado al menos 3 partidas.
    Utiliza la función `get_cartas()` para obtener los datos de la tabla `cartas`.
    Los resultados se devuelven como un diccionario para facilitar su visualización.
    """
    cartas_dict = get_cartas()  # Usamos la función ya existente para obtener los datos de las cartas

    # Verificar si tenemos datos en cartas_dict
    if not cartas_dict:
        loginfo("No se encontraron datos de cartas en la base de datos.")
        return {}

    # Consulta los jugadores que han jugado al menos 3 partidas (usando el historial)
    query_historial = """
    SELECT ID_Jugador, COUNT(DISTINCT ID_Partida) AS Partidas_Jugadas
    FROM siete_y_medio.historial
    GROUP BY ID_Jugador
    HAVING Partidas_Jugadas >= 3;
    """
    connection = connect_to_database()
    if connection:
        try:
            # Ejecutamos la consulta de jugadores con al menos 3 partidas
            jugadores_con_3_partidas = execute_query(connection, query_historial)
            close_connection(connection)

            if not jugadores_con_3_partidas:
                loginfo("No se encontraron jugadores con al menos 3 partidas jugadas.")
                return {}

            # Filtramos las cartas para los jugadores que cumplen el requisito
            resultados_dict = {}
            for jugador in jugadores_con_3_partidas:
                jugador_id = jugador['ID_Jugador']

                if jugador_id in cartas_dict:
                    carta_data = cartas_dict[jugador_id]
                    resultados_dict[jugador_id] = {
                        "ID_Jugador": jugador_id,  # Incluimos el ID del jugador
                        "Carta_Ini_POK_Mas_Repetida": carta_data['Carta_Inicial_Mas_Repetida'],
                        "Nº_Carta_Mas_Repetida": carta_data['Carta_Inicial_Mas_Repetida_XVeces'],
                        "Carta_Ini_ESP_Mas_Repetida_Palo": carta_data['Carta_Inicial_Mas_Repetida_Palo'],
                        "Nº_Carta_Palo_Repetido": carta_data['Carta_Inicial_Mas_Repetida_Palo_XVeces']
                    }

            return resultados_dict
        except Exception as e:
            loginfo(f"Error al ejecutar la consulta de jugadores con 3 o más partidas: {e}")
            return {}
    else:
        loginfo("Error: No se pudo conectar a la base de datos.")
        return {}


def apuesta_mas_alta_por_partida():
    """
    Obtiene el jugador que realizó la apuesta más alta
    en cada partida.

    Datos mostrados:
    - Identificador de la partida.
    - Identificador del jugador.
    - Monto de la apuesta más alta.
    """
    query = """
    SELECT 
        r.ID_Partida AS Identificador_Partida,
        r.ID_Jugador AS Identificador_Jugador,
        MAX(r.Apuesta) AS Apuesta_Mas_Alta
    FROM siete_y_medio.rondas r
    GROUP BY r.ID_Partida;
    """
    connection = connect_to_database()
    if connection:
        try:
            results = execute_query(connection, query)
            close_connection(connection)

            if not results:
                loginfo("No hay datos de apuestas. Asegúrese de que se hayan jugado partidas con apuestas.")
                return []

            return results
        except Exception as e:
            loginfo(f"Error al ejecutar la consulta de apuestas más altas: {e}")
            return []
    else:
        loginfo("Error: No se pudo conectar a la base de datos.")
        return []


def apuesta_mas_baja_por_partida():
    """
    Obtiene el jugador que realizó la apuesta más baja
    en cada partida.

    Datos mostrados:
    - Identificador de la partida.
    - Identificador del jugador.
    - Monto de la apuesta más baja.
    """
    query = """
    SELECT 
        r.ID_Partida AS Identificador_Partida,
        r.ID_Jugador AS Identificador_Jugador,
        MIN(r.Apuesta) AS Apuesta_Mas_Baja
    FROM siete_y_medio.rondas r
    GROUP BY r.ID_Partida;
    """
    connection = connect_to_database()
    if connection:
        try:
            results = execute_query(connection, query)
            close_connection(connection)

            if not results:
                loginfo("No hay datos de apuestas. Asegúrese de que se hayan jugado partidas con apuestas.")
                return []

            return results
        except Exception as e:
            loginfo(f"Error al ejecutar la consulta de apuestas más bajas: {e}")
            return []
    else:
        loginfo("Error: No se pudo conectar a la base de datos.")
        return []


# Carta inicial más repetida
resultados_cartas = carta_inicial_mas_repetida_con_get_cartas()
cabecera_carta = "".center(84, "-") + "\n" + "| {:<12} | {:<26} | {:<2} | {:<26} | {:<2} |".format(
    "ID Jugador",
    "Carta_Ini_POK_Mas_Repetida",
    "Nº",
    "Carta_Ini_ESP_Mas_Repetida",
    "Nº") + "\n" + "".center(84, "-")

# Iterar correctamente sobre el diccionario
if resultados_cartas:
    print(cabecera_carta)
    for jugador_id, datos in resultados_cartas.items():
        print("| {:<12} | {:<26} | {:<2} | {:<26} | {:<2} |".format(
            jugador_id,
            datos['Carta_Ini_POK_Mas_Repetida'],
            datos['Nº_Carta_Mas_Repetida'],
            datos['Carta_Ini_ESP_Mas_Repetida_Palo'],
            datos['Nº_Carta_Palo_Repetido']
        ))
    print("".center(84, "-"))
else:
    print("No hay resultados para mostrar.")


# ============================================================
# FIN DEL ARCHIVO
# ============================================================

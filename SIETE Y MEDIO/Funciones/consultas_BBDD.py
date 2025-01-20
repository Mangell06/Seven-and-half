import gestionar_base_de_datos as bbdd
import gestionar_juego as juego

# ============================================================
# CONSULTAS A LA BASE DE DATOS
# ============================================================

def carta_inicial_mas_repetida_con_get_cartas():
    """Obtiene la carta inicial más repetida por cada jugador con al menos 3 partidas."""
    cartas_dict = bbdd.get_cartas()

    if not cartas_dict:
        juego.loginfo("No se encontraron datos de cartas en la base de datos.")
        return {}

    query_historial = """
    SELECT ID_Jugador, COUNT(DISTINCT ID_Partida) AS Partidas_Jugadas
    FROM siete_y_medio.historial
    GROUP BY ID_Jugador
    HAVING Partidas_Jugadas >= 3;
    """
    connection = bbdd.connect_to_database()
    if connection:
        try:
            jugadores_con_3_partidas = bbdd.execute_query(connection, query_historial)
            bbdd.close_connection(connection)

            if not jugadores_con_3_partidas:
                juego.loginfo("No se encontraron jugadores con al menos 3 partidas jugadas.")
                return {}

            # Cabecera de la tabla
            cabecera_carta = "".center(84, "-") + "\n" + "| {:<12} | {:<26} | {:<2} | {:<26} | {:<2} |".format(
                "ID Jugador",
                "Carta_Ini_POK_Mas_Repetida",
                "Nº",
                "Carta_Ini_ESP_Mas_Repetida",
                "Nº") + "\n" + "".center(84, "-")

            # Mostrar la cabecera
            print(cabecera_carta)

            resultados_dict = {}
            for jugador in jugadores_con_3_partidas:
                jugador_id = jugador['ID_Jugador']
                if jugador_id in cartas_dict:
                    carta_data = cartas_dict[jugador_id]
                    resultados_dict[jugador_id] = {
                        "ID_Jugador": jugador_id,
                        "Carta_Ini_POK_Mas_Repetida": carta_data['Carta_Inicial_Mas_Repetida'],
                        "Nº_Carta_Mas_Repetida": carta_data['Carta_Inicial_Mas_Repetida_XVeces'],
                        "Carta_Ini_ESP_Mas_Repetida_Palo": carta_data['Carta_Inicial_Mas_Repetida_Palo'],
                        "Nº_Carta_Palo_Repetido": carta_data['Carta_Inicial_Mas_Repetida_Palo_XVeces'],
                    }

                    # Imprimir cada fila de la tabla
                    print("| {:<12} | {:<26} | {:<2} | {:<26} | {:<2} |".format(
                        jugador_id,
                        carta_data['Carta_Inicial_Mas_Repetida'],
                        carta_data['Carta_Inicial_Mas_Repetida_XVeces'],
                        carta_data['Carta_Inicial_Mas_Repetida_Palo'],
                        carta_data['Carta_Inicial_Mas_Repetida_Palo_XVeces']
                    ))

            print("".center(84, "-"))

        except Exception as e:
            juego.loginfo(f"Error al ejecutar la consulta: {e}")
            return {}
    else:
        juego.loginfo("Error: No se pudo conectar a la base de datos.")
        return {}


def jugador_apuesta_mas_alta_por_partida():
    """Obtiene el jugador que realizó la apuesta más alta en cada partida."""
    query_rondas = """
    SELECT 
        ID_Partida,
        ID_Jugador,
        Apuesta
    FROM 
        siete_y_medio.rondas
    WHERE (ID_Partida, Apuesta) IN (
        SELECT 
            ID_Partida,
            MAX(Apuesta) AS Apuesta_Mas_Alta
        FROM 
            siete_y_medio.rondas
        GROUP BY 
            ID_Partida
    );
    """

    connection = bbdd.connect_to_database()
    if connection:
        try:
            # Ejecutar la consulta para obtener al jugador con la apuesta más alta por partida
            rondas_resultados = bbdd.execute_query(connection, query_rondas)
            bbdd.close_connection(connection)

            if not rondas_resultados:
                juego.loginfo("No se encontraron resultados de rondas en la base de datos.")
                return {}

            # Cabecera de la tabla
            cabecera_apuestas = "".center(52, "-") + "\n" + "| {:<12} | {:<12} | {:<18} |".format(
                "ID Partida",
                "ID Jugador",
                "Apuesta Más Alta") + "\n" + "".center(52, "-")

            # Mostrar la cabecera
            print(cabecera_apuestas)

            # Iterar sobre los resultados y mostrar la información
            for ronda in rondas_resultados:
                partida_id = ronda['ID_Partida']
                jugador_id = ronda['ID_Jugador']
                apuesta_mas_alta = ronda['Apuesta']

                # Imprimir cada fila de la tabla
                print("| {:<12} | {:<12} | {:<18} |".format(
                    partida_id,
                    jugador_id,
                    apuesta_mas_alta
                ))

            print("".center(52, "-"))

        except Exception as e:
            juego.loginfo(f"Error al ejecutar la consulta: {e}")
            return {}
    else:
        juego.loginfo("Error: No se pudo conectar a la base de datos.")
        return {}


def jugador_apuesta_mas_baja_por_partida():
    """Obtiene el jugador que realizó la apuesta más baja en cada partida."""
    query_rondas = """
    SELECT 
        ID_Partida,
        ID_Jugador,
        Apuesta
    FROM 
        siete_y_medio.rondas
    WHERE (ID_Partida, Apuesta) IN (
        SELECT 
            ID_Partida,
            MIN(Apuesta) AS Apuesta_Mas_Baja
        FROM 
            siete_y_medio.rondas
        GROUP BY 
            ID_Partida
    );
    """

    connection = bbdd.connect_to_database()
    if connection:
        try:
            # Ejecutar la consulta para obtener al jugador con la apuesta más baja por partida
            rondas_resultados = bbdd.execute_query(connection, query_rondas)
            bbdd.close_connection(connection)

            if not rondas_resultados:
                juego.loginfo("No se encontraron resultados de rondas en la base de datos.")
                return {}

            # Cabecera de la tabla
            cabecera_apuestas_baja = "".center(52, "-") + "\n" + "| {:<12} | {:<12} | {:<18} |".format(
                "ID Partida",
                "ID Jugador",
                "Apuesta Más Baja") + "\n" + "".center(52, "-")

            # Mostrar la cabecera
            print(cabecera_apuestas_baja)

            # Iterar sobre los resultados y mostrar la información
            for ronda in rondas_resultados:
                partida_id = ronda['ID_Partida']
                jugador_id = ronda['ID_Jugador']
                apuesta_mas_baja = ronda['Apuesta']

                # Imprimir cada fila de la tabla
                print("| {:<12} | {:<12} | {:<18} |".format(
                    partida_id,
                    jugador_id,
                    apuesta_mas_baja
                ))

            print("".center(52, "-"))

        except Exception as e:
            juego.loginfo(f"Error al ejecutar la consulta: {e}")
            return {}
    else:
        juego.loginfo("Error: No se pudo conectar a la base de datos.")
        return {}


# ============================================================
# FIN DEL ARCHIVO
# ============================================================

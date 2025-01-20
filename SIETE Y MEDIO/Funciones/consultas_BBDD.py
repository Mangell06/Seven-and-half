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
            return resultados_dict
        except Exception as e:
            juego.loginfo(f"Error al ejecutar la consulta: {e}")
            return {}
    else:
        juego.loginfo("Error: No se pudo conectar a la base de datos.")
        return {}


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

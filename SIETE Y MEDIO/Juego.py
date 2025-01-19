#Diccionario Cartas
from datetime import datetime

cartas_game = {

    #BARAJA ESPAÑOLA:

    #OROS
    "EO1": {"literal": "As de Oros", "value": 1, "priority": 1, "realValue": 1},
    "EO2": {"literal": "Dos de Oros", "value": 2, "priority": 1, "realValue": 2},
    "EO3": {"literal": "Tres de Oros", "value": 3, "priority": 1, "realValue": 3},
    "EO4": {"literal": "Cuatro de Oros", "value": 4, "priority": 1, "realValue": 4},
    "EO5": {"literal": "Cinco de Oros", "value": 5, "priority": 1, "realValue": 5},
    "EO6": {"literal": "Seis de Oros", "value": 6, "priority": 1, "realValue": 6},
    "EO7": {"literal": "Siete de Oros", "value": 7, "priority": 1, "realValue": 7},
    "EO8": {"literal": "Ocho de Oros", "value": 0.5, "priority": 1, "realValue": 8},
    "EO9": {"literal": "Nueve de Oros", "value": 0.5, "priority": 1, "realValue": 9},
    "EO10": {"literal": "Diez de Oros", "value": 0.5, "priority": 1, "realValue": 10},
    "EO11": {"literal": "Sota de Oros", "value": 0.5, "priority": 1, "realValue": 11},
    "EO12": {"literal": "Caballo de Oros", "value": 0.5, "priority": 1, "realValue": 12},
    "EO13": {"literal": "Rey de Oros", "value": 0.5, "priority": 1, "realValue": 13},
    #COPAS
    "EC1": {"literal": "As de Copas", "value": 1, "priority": 2, "realValue": 1},
    "EC2": {"literal": "Dos de Copas", "value": 2, "priority": 2, "realValue": 2},
    "EC3": {"literal": "Tres de Copas", "value": 3, "priority": 2, "realValue": 3},
    "EC4": {"literal": "Cuatro de Copas", "value": 4, "priority": 2, "realValue": 4},
    "EC5": {"literal": "Cinco de Copas", "value": 5, "priority": 2, "realValue": 5},
    "EC6": {"literal": "Seis de Copas", "value": 6, "priority": 2, "realValue": 6},
    "EC7": {"literal": "Siete de Copas", "value": 7, "priority": 2, "realValue": 7},
    "EC8": {"literal": "Ocho de Copas", "value": 0.5, "priority": 2, "realValue": 8},
    "EC9": {"literal": "Nueve de Copas", "value": 0.5, "priority": 2, "realValue": 9},
    "EC10": {"literal": "Diez de Copas", "value": 0.5, "priority": 2, "realValue": 10},
    "EC11": {"literal": "Sota de Copas", "value": 0.5, "priority": 2, "realValue": 11},
    "EC12": {"literal": "Caballo de Copas", "value": 0.5, "priority": 2, "realValue": 12},
    "EC13": {"literal": "Rey de Copas", "value": 0.5, "priority": 2, "realValue": 13},
    #ESPADAS
    "EE1": {"literal": "As de Espadas", "value": 1, "priority": 3, "realValue": 1},
    "EE2": {"literal": "Dos de Espadas", "value": 2, "priority": 3, "realValue": 2},
    "EE3": {"literal": "Tres de Espadas", "value": 3, "priority": 3, "realValue": 3},
    "EE4": {"literal": "Cuatro de Espadas", "value": 4, "priority": 3, "realValue": 4},
    "EE5": {"literal": "Cinco de Espadas", "value": 5, "priority": 3, "realValue": 5},
    "EE6": {"literal": "Seis de Espadas", "value": 6, "priority": 3, "realValue": 6},
    "EE7": {"literal": "Siete de Espadas", "value": 7, "priority": 3, "realValue": 7},
    "EE8": {"literal": "Ocho de Espadas", "value": 0.5, "priority": 3, "realValue": 8},
    "EE9": {"literal": "Nueve de Espadas", "value": 0.5, "priority": 3, "realValue": 9},
    "EE10": {"literal": "Diez de Espadas", "value": 0.5, "priority": 3, "realValue": 10},
    "EE11": {"literal": "Sota de Espadas", "value": 0.5, "priority": 3, "realValue": 11},
    "EE12": {"literal": "Caballo de Espadas", "value": 0.5, "priority": 3, "realValue": 12},
    "EE13": {"literal": "Rey de Espadas", "value": 0.5, "priority": 3, "realValue": 13},
    #BASTONES
    "EB1": {"literal": "As de Bastos", "value": 1, "priority": 4, "realValue": 1},
    "EB2": {"literal": "Dos de Bastos", "value": 2, "priority": 4, "realValue": 2},
    "EB3": {"literal": "Tres de Bastos", "value": 3, "priority": 4, "realValue": 3},
    "EB4": {"literal": "Cuatro de Bastos", "value": 4, "priority": 4, "realValue": 4},
    "EB5": {"literal": "Cinco de Bastos", "value": 5, "priority": 4, "realValue": 5},
    "EB6": {"literal": "Seis de Bastos", "value": 6, "priority": 4, "realValue": 6},
    "EB7": {"literal": "Siete de Bastos", "value": 7, "priority": 4, "realValue": 7},
    "EB8": {"literal": "Ocho de Bastos", "value": 0.5, "priority": 4, "realValue": 8},
    "EB9": {"literal": "Nueve de Bastos", "value": 0.5, "priority": 4, "realValue": 9},
    "EB10": {"literal": "Diez de Bastos", "value": 0.5, "priority": 4, "realValue": 10},
    "EB11": {"literal": "Sota de Bastos", "value": 0.5, "priority": 4, "realValue": 11},
    "EB12": {"literal": "Caballo de Bastos", "value": 0.5, "priority": 4, "realValue": 12},
    "EB13": {"literal": "Rey de Bastos", "value": 0.5, "priority": 4, "realValue": 13},

    #BARAJA POKER:

    #DIAMANTES
    "PD1": {"literal": "As de Diamantes", "value": 1, "priority": 1, "realValue": 1},
    "PD2": {"literal": "Dos de Diamantes", "value": 2, "priority": 1, "realValue": 2},
    "PD3": {"literal": "Tres de Diamantes", "value": 3, "priority": 1, "realValue": 3},
    "PD4": {"literal": "Cuatro de Diamantes", "value": 4, "priority": 1, "realValue": 4},
    "PD5": {"literal": "Cinco de Diamantes", "value": 5, "priority": 1, "realValue": 5},
    "PD6": {"literal": "Seis de Diamantes", "value": 6, "priority": 1, "realValue": 6},
    "PD7": {"literal": "Siete de Diamantes", "value": 7, "priority": 1, "realValue": 7},
    "PD8": {"literal": "Ocho de Diamantes", "value": 0.5, "priority": 1, "realValue": 8},
    "PD9": {"literal": "Nueve de Diamantes", "value": 0.5, "priority": 1, "realValue": 9},
    "PD10": {"literal": "Diez de Diamantes", "value": 0.5, "priority": 1, "realValue": 10},
    "PD11": {"literal": "Jota de Diamantes", "value": 0.5, "priority": 1, "realValue": 11},
    "PD12": {"literal": "Reina de Diamantes", "value": 0.5, "priority": 1, "realValue": 12},
    "PD13": {"literal": "Rey de Diamantes", "value": 0.5, "priority": 1, "realValue": 13},
    #CORAZONES
    "PC1": {"literal": "As de Corazones", "value": 1, "priority": 2, "realValue": 1},
    "PC2": {"literal": "Dos de Corazones", "value": 2, "priority": 2, "realValue": 2},
    "PC3": {"literal": "Tres de Corazones", "value": 3, "priority": 2, "realValue": 3},
    "PC4": {"literal": "Cuatro de Corazones", "value": 4, "priority": 2, "realValue": 4},
    "PC5": {"literal": "Cinco de Corazones", "value": 5, "priority": 2, "realValue": 5},
    "PC6": {"literal": "Seis de Corazones", "value": 6, "priority": 2, "realValue": 6},
    "PC7": {"literal": "Siete de Corazones", "value": 7, "priority": 2, "realValue": 7},
    "PC8": {"literal": "Ocho de Corazones", "value": 0.5, "priority": 2, "realValue": 8},
    "PC9": {"literal": "Nueve de Corazones", "value": 0.5, "priority": 2, "realValue": 9},
    "PC10": {"literal": "Diez de Corazones", "value": 0.5, "priority": 2, "realValue": 10},
    "PC11": {"literal": "Jota de Corazones", "value": 0.5, "priority": 2, "realValue": 11},
    "PC12": {"literal": "Reina de Corazones", "value": 0.5, "priority": 2, "realValue": 12},
    "PC13": {"literal": "Rey de Corazones", "value": 0.5, "priority": 2, "realValue": 13},
    #PICAS
    "PP1": {"literal": "As de Picas", "value": 1, "priority": 3, "realValue": 1},
    "PP2": {"literal": "Dos de Picas", "value": 2, "priority": 3, "realValue": 2},
    "PP3": {"literal": "Tres de Picas", "value": 3, "priority": 3, "realValue": 3},
    "PP4": {"literal": "Cuatro de Picas", "value": 4, "priority": 3, "realValue": 4},
    "PP5": {"literal": "Cinco de Picas", "value": 5, "priority": 3, "realValue": 5},
    "PP6": {"literal": "Seis de Picas", "value": 6, "priority": 3, "realValue": 6},
    "PP7": {"literal": "Siete de Picas", "value": 7, "priority": 3, "realValue": 7},
    "PP8": {"literal": "Ocho de Picas", "value": 0.5, "priority": 3, "realValue": 8},
    "PP9": {"literal": "Nueve de Picas", "value": 0.5, "priority": 3, "realValue": 9},
    "PP10": {"literal": "Diez de Picas", "value": 0.5, "priority": 3, "realValue": 10},
    "PP11": {"literal": "Jota de Picas", "value": 0.5, "priority": 3, "realValue": 11},
    "PP12": {"literal": "Reina de Picas", "value": 0.5, "priority": 3, "realValue": 12},
    "PP13": {"literal": "Rey de Picas", "value": 0.5, "priority": 3, "realValue": 13},
    #TREBOLES
    "PT1": {"literal": "As de Tréboles", "value": 1, "priority": 4, "realValue": 1},
    "PT2": {"literal": "Dos de Tréboles", "value": 2, "priority": 4, "realValue": 2},
    "PT3": {"literal": "Tres de Tréboles", "value": 3, "priority": 4, "realValue": 3},
    "PT4": {"literal": "Cuatro de Tréboles", "value": 4, "priority": 4, "realValue": 4},
    "PT5": {"literal": "Cinco de Tréboles", "value": 5, "priority": 4, "realValue": 5},
    "PT6": {"literal": "Seis de Tréboles", "value": 6, "priority": 4, "realValue": 6},
    "PT7": {"literal": "Siete de Tréboles", "value": 7, "priority": 4, "realValue": 7},
    "PT8": {"literal": "Ocho de Tréboles", "value": 0.5, "priority": 4, "realValue": 8},
    "PT9": {"literal": "Nueve de Tréboles", "value": 0.5, "priority": 4, "realValue": 9},
    "PT10": {"literal": "Diez de Tréboles", "value": 0.5, "priority": 4, "realValue": 10},
    "PT11": {"literal": "Jota de Tréboles", "value": 0.5, "priority": 4, "realValue": 11},
    "PT12": {"literal": "Reina de Tréboles", "value": 0.5, "priority": 4, "realValue": 12},
    "PT13": {"literal": "Rey de Tréboles", "value": 0.5, "priority": 4, "realValue": 13}
}

#Importaciones:
import Funciones.gestionar_interfaz as interface
import Funciones.gestionar_juego as juego
import Funciones.gestionar_diccionarios as diccionarios
import Funciones.gestionar_base_de_datos as bbdd

#Mensaje del log cuando inicia el juego
juego.loginfo("[Juego Iniciado]")

#Sacar diccionarios de la base de datos
players_dicti = bbdd.get_personajes()
cartas_dicti = bbdd.get_cartas()
historial_dicti = bbdd.get_historial()
partidas_dicti = bbdd.get_partidas()

#Sacar listas de keys de los diccionarios
players_list = []
for key in players_dicti:
    players_list.append(key)

jugando = []
for key in players_dicti:
    if players_dicti[key]["In_Game"]:
        jugando.append(key)

#Flags
flg_salir = False
flg_00 = True
flg_01 = False
flg_02 = False
flg_04 = False
flg_05 = False

#Menus
menu00 = ("Siete y medio","Esteve Terradas","Añadir/Eliminar/Ver Jugadores",
          "Ajustes","Jugar","Ranking","Reportes","Salir")
menu01 = ("BBDD Jugadores","Nuevo Humano","Nuevo Bot","Ver/Eliminar Jugadores",
          "Volver atras")
menu02 = ("Ajustes","Elegir jugadores jugando","Elegir Mazo",
          "Elegir ronda maxima (Por defecto 5 Rondas)","Volver atras")
menu04 = ("Ranking","Players With More Earnings","Players With More Games Played",
          "Players With More Minutes Played","Go back")
menu05 = ("Reports","1","2","3","4","5","6","7","Go back")

set_cartas = ("Elige una carta","Española","Poker")

new_party = {len(partidas_dicti) + 1: {
    "start_date": "",
    "end_date": "",
    "ID_Ganador": "",
    "Total_Rondas": 5,
    "Mazo": "",
    "Players":[]}}

#Estructura {0:{"DNI":{"Puntos_iniciales":20,"Puntos_finales":55,"Carta_inicial":""},
#               "DNI":{"Puntos_iniciales":29,"Puntos_finales":4,"Carta_inicial":""}}}
player_party = {}

#Estrucuta {"DNI":{Cartas_iniciales_esp:[[EO1,2],[EC3,1]],Cartas_iniciales_pk:[[PD1,5],[PC5,10]]}
card_initial = {}

#Estructura {0:{"DNI":{"Es_banca":True,"Apuesta":14,"Puntos_inciales":30,Valor_total_cartas:7.5,"Puntos_finales":44},
#               "DNI"{"Es_banca":False,"Apuesta":14,"Puntos_inciales":20,Valor_total_cartas:7,"Puntos_finales":6}}}
player_round = {}

while not flg_salir:
    while flg_00:
        print(new_party)
        players_dicti = bbdd.get_personajes()
        opc = interface.management_menu(title=2,menu=menu00)
        if opc == 1:
            flg_00 = False
            flg_01 = True
        elif opc == 2:
            flg_00 = False
            flg_02 = True
        elif opc == 3:
            if new_party[len(partidas_dicti) + 1]["Mazo"] == "":
                print("Elige un mazo con el que jugar en settings".center(50))
                input("Presiona enter para continuar".center(50))
            else:
                new_party[len(partidas_dicti) + 1]["start_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_party[len(partidas_dicti) + 1]["Players"] = jugando
                mazo = juego.crearmazo(partidas_dicti,new_party,cartas_game)
            for i in range(len(jugando)):
                player_party[players_dicti[jugando[i]]] = {"Es banca":False,"Apuesta":0,"Puntos_iniciales":partidas_dicti[jugando[i]]["Puntos"],"Valor_total_cartas":0,"puntos_finales":0}
        elif opc == 4:
            flg_00 = False
            flg_04 = True
        elif opc == 5:
            flg_00 = False
            flg_05 = True
        else:
            juego.loginfo("[Saliendo del Juego]")
            flg_00 = False
            flg_salir = True

    while flg_01:
        players_dicti = bbdd.get_personajes()
        opc = interface.management_menu(title=1,menu=menu01)
        if opc == 1:
            diccionarios.nuevohumano(players_dicti)
        elif opc == 2:
            diccionarios.nuevobot(players_dicti)
        elif opc == 3:
            diccionarios.showplayer(players_dicti)
        else:
            flg_01 = False
            flg_00 = True

    while flg_02:
        players_dicti = bbdd.get_personajes()
        opc = interface.management_menu(title=1,menu=menu02)
        if opc == 1:
            jugando = juego.elegirpersonajejugar(players_dicti)
            for key in players_dicti:
                if key in jugando:
                    players_dicti[key]["In_Game"] = True
                else:
                    players_dicti[key]["In_Game"] = False
        elif opc == 2:
            players_dicti = bbdd.get_personajes()
            aux = interface.management_menu(title=1,menu=set_cartas)
            if aux == 1:
                new_party[len(partidas_dicti)+1]["Mazo"] = "Española"
            else:
                new_party[len(partidas_dicti)+1]["Mazo"] = "Poker"
            aux = "Mazo establecido: {}".format(new_party[len(partidas_dicti)+1]["Mazo"])
            print(aux.center(50))
            input("Presiona enter para continuar".center(50))
        elif opc == 3:
            aux = juego.rondamaxima()
            new_party[len(partidas_dicti)+1]["ID_Ganador"] = aux
        else:
            flg_02 = False
            flg_00 = True

    while flg_04:
        players_dicti = bbdd.get_personajes()
        opc = interface.management_menu(title=1,menu=menu04)
        if opc == 1:
            juego.raking_id(players_dicti)
        elif opc == 2:
            juego.raking_puntos(players_dicti)
        elif opc == 3:
            juego.raking_minuts_played(players_dicti)
        else:
            flg_04 = False
            flg_00 = True

    while flg_05:
        opc = interface.management_menu(title=1,menu=menu05)
        if opc == 1:
            print(1)
        elif opc == 2:
            print(2)
        elif opc == 3:
            print(3)
        elif opc == 4:
            print(4)
        elif opc == 5:
            print(5)
        elif opc == 6:
            print(6)
        elif opc == 7:
            print(7)
        else:
            flg_05 = False
            flg_00 = True
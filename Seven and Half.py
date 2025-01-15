#Importaciones:
import FUCTIONS.MANAGEMENT as manage
from FUCTIONS.MANAGEMENT import loginfo

#Diccionario Cartas
cartas = {

    #BARAJA ESPAÑOLA:

    #OROS
    "O101": {"literal": "As de Oros", "value": 1, "priority": 1, "realValue": 1},
    "O102": {"literal": "Dos de Oros", "value": 2, "priority": 1, "realValue": 2},
    "O103": {"literal": "Tres de Oros", "value": 3, "priority": 1, "realValue": 3},
    "O104": {"literal": "Cuatro de Oros", "value": 4, "priority": 1, "realValue": 4},
    "O105": {"literal": "Cinco de Oros", "value": 5, "priority": 1, "realValue": 5},
    "O106": {"literal": "Seis de Oros", "value": 6, "priority": 1, "realValue": 6},
    "O107": {"literal": "Siete de Oros", "value": 7, "priority": 1, "realValue": 7},
    "O108": {"literal": "Ocho de Oros", "value": 0.5, "priority": 1, "realValue": 8},
    "O109": {"literal": "Nueve de Oros", "value": 0.5, "priority": 1, "realValue": 9},
    "O110": {"literal": "Diez de Oros", "value": 0.5, "priority": 1, "realValue": 10},
    "O111": {"literal": "Sota de Oros", "value": 0.5, "priority": 1, "realValue": 11},
    "O112": {"literal": "Caballo de Oros", "value": 0.5, "priority": 1, "realValue": 12},
    "O113": {"literal": "Rey de Oros", "value": 0.5, "priority": 1, "realValue": 13},
    #COPAS
    "C101": {"literal": "As de Copas", "value": 1, "priority": 2, "realValue": 1},
    "C102": {"literal": "Dos de Copas", "value": 2, "priority": 2, "realValue": 2},
    "C103": {"literal": "Tres de Copas", "value": 3, "priority": 2, "realValue": 3},
    "C104": {"literal": "Cuatro de Copas", "value": 4, "priority": 2, "realValue": 4},
    "C105": {"literal": "Cinco de Copas", "value": 5, "priority": 2, "realValue": 5},
    "C106": {"literal": "Seis de Copas", "value": 6, "priority": 2, "realValue": 6},
    "C107": {"literal": "Siete de Copas", "value": 7, "priority": 2, "realValue": 7},
    "C108": {"literal": "Ocho de Copas", "value": 0.5, "priority": 2, "realValue": 8},
    "C109": {"literal": "Nueve de Copas", "value": 0.5, "priority": 2, "realValue": 9},
    "C110": {"literal": "Diez de Copas", "value": 0.5, "priority": 2, "realValue": 10},
    "C111": {"literal": "Sota de Copas", "value": 0.5, "priority": 2, "realValue": 11},
    "C112": {"literal": "Caballo de Copas", "value": 0.5, "priority": 2, "realValue": 12},
    "C113": {"literal": "Rey de Copas", "value": 0.5, "priority": 2, "realValue": 13},
    #ESPADAS
    "E101": {"literal": "As de Espadas", "value": 1, "priority": 3, "realValue": 1},
    "E102": {"literal": "Dos de Espadas", "value": 2, "priority": 3, "realValue": 2},
    "E103": {"literal": "Tres de Espadas", "value": 3, "priority": 3, "realValue": 3},
    "E104": {"literal": "Cuatro de Espadas", "value": 4, "priority": 3, "realValue": 4},
    "E105": {"literal": "Cinco de Espadas", "value": 5, "priority": 3, "realValue": 5},
    "E106": {"literal": "Seis de Espadas", "value": 6, "priority": 3, "realValue": 6},
    "E107": {"literal": "Siete de Espadas", "value": 7, "priority": 3, "realValue": 7},
    "E108": {"literal": "Ocho de Espadas", "value": 0.5, "priority": 3, "realValue": 8},
    "E109": {"literal": "Nueve de Espadas", "value": 0.5, "priority": 3, "realValue": 9},
    "E110": {"literal": "Diez de Espadas", "value": 0.5, "priority": 3, "realValue": 10},
    "E111": {"literal": "Sota de Espadas", "value": 0.5, "priority": 3, "realValue": 11},
    "E112": {"literal": "Caballo de Espadas", "value": 0.5, "priority": 3, "realValue": 12},
    "E113": {"literal": "Rey de Espadas", "value": 0.5, "priority": 3, "realValue": 13},
    #BASTONES
    "B101": {"literal": "As de Bastos", "value": 1, "priority": 4, "realValue": 1},
    "B102": {"literal": "Dos de Bastos", "value": 2, "priority": 4, "realValue": 2},
    "B103": {"literal": "Tres de Bastos", "value": 3, "priority": 4, "realValue": 3},
    "B104": {"literal": "Cuatro de Bastos", "value": 4, "priority": 4, "realValue": 4},
    "B105": {"literal": "Cinco de Bastos", "value": 5, "priority": 4, "realValue": 5},
    "B106": {"literal": "Seis de Bastos", "value": 6, "priority": 4, "realValue": 6},
    "B107": {"literal": "Siete de Bastos", "value": 7, "priority": 4, "realValue": 7},
    "B108": {"literal": "Ocho de Bastos", "value": 0.5, "priority": 4, "realValue": 8},
    "B109": {"literal": "Nueve de Bastos", "value": 0.5, "priority": 4, "realValue": 9},
    "B110": {"literal": "Diez de Bastos", "value": 0.5, "priority": 4, "realValue": 10},
    "B111": {"literal": "Sota de Bastos", "value": 0.5, "priority": 4, "realValue": 11},
    "B112": {"literal": "Caballo de Bastos", "value": 0.5, "priority": 4, "realValue": 12},
    "B113": {"literal": "Rey de Bastos", "value": 0.5, "priority": 4, "realValue": 13},

    #BARAJA POKER:

    #DIAMANTES
    "D201": {"literal": "As de Diamantes", "value": 1, "priority": 1, "realValue": 1},
    "D202": {"literal": "Dos de Diamantes", "value": 2, "priority": 1, "realValue": 2},
    "D203": {"literal": "Tres de Diamantes", "value": 3, "priority": 1, "realValue": 3},
    "D204": {"literal": "Cuatro de Diamantes", "value": 4, "priority": 1, "realValue": 4},
    "D205": {"literal": "Cinco de Diamantes", "value": 5, "priority": 1, "realValue": 5},
    "D206": {"literal": "Seis de Diamantes", "value": 6, "priority": 1, "realValue": 6},
    "D207": {"literal": "Siete de Diamantes", "value": 7, "priority": 1, "realValue": 7},
    "D208": {"literal": "Ocho de Diamantes", "value": 0.5, "priority": 1, "realValue": 8},
    "D209": {"literal": "Nueve de Diamantes", "value": 0.5, "priority": 1, "realValue": 9},
    "D210": {"literal": "Diez de Diamantes", "value": 0.5, "priority": 1, "realValue": 10},
    "D211": {"literal": "Jota de Diamantes", "value": 0.5, "priority": 1, "realValue": 11},
    "D212": {"literal": "Reina de Diamantes", "value": 0.5, "priority": 1, "realValue": 12},
    "D213": {"literal": "Rey de Diamantes", "value": 0.5, "priority": 1, "realValue": 13},
    #CORAZONES
    "C201": {"literal": "As de Corazones", "value": 1, "priority": 2, "realValue": 1},
    "C202": {"literal": "Dos de Corazones", "value": 2, "priority": 2, "realValue": 2},
    "C203": {"literal": "Tres de Corazones", "value": 3, "priority": 2, "realValue": 3},
    "C204": {"literal": "Cuatro de Corazones", "value": 4, "priority": 2, "realValue": 4},
    "C205": {"literal": "Cinco de Corazones", "value": 5, "priority": 2, "realValue": 5},
    "C206": {"literal": "Seis de Corazones", "value": 6, "priority": 2, "realValue": 6},
    "C207": {"literal": "Siete de Corazones", "value": 7, "priority": 2, "realValue": 7},
    "C208": {"literal": "Ocho de Corazones", "value": 0.5, "priority": 2, "realValue": 8},
    "C209": {"literal": "Nueve de Corazones", "value": 0.5, "priority": 2, "realValue": 9},
    "C210": {"literal": "Diez de Corazones", "value": 0.5, "priority": 2, "realValue": 10},
    "C211": {"literal": "Jota de Corazones", "value": 0.5, "priority": 2, "realValue": 11},
    "C212": {"literal": "Reina de Corazones", "value": 0.5, "priority": 2, "realValue": 12},
    "C213": {"literal": "Rey de Corazones", "value": 0.5, "priority": 2, "realValue": 13},
    #PICAS
    "P201": {"literal": "As de Picas", "value": 1, "priority": 3, "realValue": 1},
    "P202": {"literal": "Dos de Picas", "value": 2, "priority": 3, "realValue": 2},
    "P203": {"literal": "Tres de Picas", "value": 3, "priority": 3, "realValue": 3},
    "P204": {"literal": "Cuatro de Picas", "value": 4, "priority": 3, "realValue": 4},
    "P205": {"literal": "Cinco de Picas", "value": 5, "priority": 3, "realValue": 5},
    "P206": {"literal": "Seis de Picas", "value": 6, "priority": 3, "realValue": 6},
    "P207": {"literal": "Siete de Picas", "value": 7, "priority": 3, "realValue": 7},
    "P208": {"literal": "Ocho de Picas", "value": 0.5, "priority": 3, "realValue": 8},
    "P209": {"literal": "Nueve de Picas", "value": 0.5, "priority": 3, "realValue": 9},
    "P210": {"literal": "Diez de Picas", "value": 0.5, "priority": 3, "realValue": 10},
    "P211": {"literal": "Jota de Picas", "value": 0.5, "priority": 3, "realValue": 11},
    "P212": {"literal": "Reina de Picas", "value": 0.5, "priority": 3, "realValue": 12},
    "P213": {"literal": "Rey de Picas", "value": 0.5, "priority": 3, "realValue": 13},
    #TREBOLES
    "T201": {"literal": "As de Tréboles", "value": 1, "priority": 4, "realValue": 1},
    "T202": {"literal": "Dos de Tréboles", "value": 2, "priority": 4, "realValue": 2},
    "T203": {"literal": "Tres de Tréboles", "value": 3, "priority": 4, "realValue": 3},
    "T204": {"literal": "Cuatro de Tréboles", "value": 4, "priority": 4, "realValue": 4},
    "T205": {"literal": "Cinco de Tréboles", "value": 5, "priority": 4, "realValue": 5},
    "T206": {"literal": "Seis de Tréboles", "value": 6, "priority": 4, "realValue": 6},
    "T207": {"literal": "Siete de Tréboles", "value": 7, "priority": 4, "realValue": 7},
    "T208": {"literal": "Ocho de Tréboles", "value": 0.5, "priority": 4, "realValue": 8},
    "T209": {"literal": "Nueve de Tréboles", "value": 0.5, "priority": 4, "realValue": 9},
    "T210": {"literal": "Diez de Tréboles", "value": 0.5, "priority": 4, "realValue": 10},
    "T211": {"literal": "Jota de Tréboles", "value": 0.5, "priority": 4, "realValue": 11},
    "T212": {"literal": "Reina de Tréboles", "value": 0.5, "priority": 4, "realValue": 12},
    "T213": {"literal": "Rey de Tréboles", "value": 0.5, "priority": 4, "realValue": 13}
}


#Diccionario para jugadores.
players = {}

#Lista para las keys de jugadores.
game=[]

#Añadir Keys de los jugadores a la lista.
if len(players) != 0:
    for key in players:
        game.append(key)

#Menus
menu_principal = ("Siete y medio","Esteve Terradas","Add/Remove/Show Players",
                  "Settings","Play Game","Ranking","Reports","Exit")

menu_bbdd_players = ("BBDD Players","New Human Player","New Boot","Show/Remove Players",
                     "Go back")

menu_settings = ("Settings","Set Game Players","Set Card's Deck",
                 "Set Max Rounds (Default 5 Rounds)","Go back")

menu_ranking = ("Ranking","Players With More Earnings","Players With More Games Played",
                "Players With More Minutes Played","Go back")

menu_reports = ("Reports","1","2","3","4","5","6","7","Go back")

#Flags
flg_salir = False
flg_00 = True
flg_01 = False
flg_02 = False
flg_04 = False
flg_05 = False

#Seleccionar tipos de cartas.
select_cartas = "Español"

#Variable booleana para saber si ya estamos a la mitad de las cartas.
poder = False

#Diccionario para las keys de las cartas.
mazo = []

#Añadir las keys de las cartas a la lista.
for key in cartas:
    if select_cartas == "Español":
        if len(mazo) != 52:
            mazo.append(key)
    else:
        if key == "D201":
            poder = True
        if poder:
            mazo.append(key)

#Inicio
loginfo("\n[Juego Iniciado]")

while not flg_salir:
    while flg_00:
        opc = manage.management_menu(title=2,menu=menu_principal)
        if opc == 1:
            flg_01 = True
            flg_00 = False
        elif opc == 2:
            flg_02 = True
            flg_00 = False
        elif opc == 3:
            print(3)
        elif opc == 4:
            flg_04 = True
            flg_00 = False
        elif opc == 5:
            flg_05 = True
            flg_00 = False
        else:
            flg_salir = True
            flg_00 = False
    while flg_02:
        opc = manage.management_menu(title=1,menu=menu_settings)
        if opc == 1:
            print(1)
        elif opc == 2:
            print(2)
        elif opc == 3:
            print(3)
        else:
            flg_00 = True
            flg_02 = False
    while flg_01:
        opc = manage.management_menu(title=1,menu=menu_bbdd_players)
        if opc == 1:
            print(1)
        elif opc == 2:
            print(2)
        elif opc == 3:
            print(3)
        else:
            flg_00 = True
            flg_01 = False
    while flg_04:
        opc = manage.management_menu(title=1,menu=menu_ranking)
        if opc == 1:
            print(1)
        elif opc == 2:
            print(2)
        elif opc == 3:
            print(3)
        else:
            flg_00 = True
            flg_04 = False
    while flg_05:
        opc = manage.management_menu(title=1,menu=menu_reports)
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
            flg_00 = True
            flg_05 = False


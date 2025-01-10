#Archivo Base del video juego.

#Funciones importadas
import FUCTIONS.INTERFACE_FUCTIONS.Create_Menu as Create_Menus

#Variables
title_game = (
    "  _____                          ___              __   __  __      ______",
    " / ___/ ___ _   _____  ____     /   |  ____  ____/ /  / / / /___ _/ / __/ ",
    " \\__ \\_/ _ \\ | / / _ \\/ __ \\   / /| | / __ \\/ __  /  / /_/ / __ `/ / /_   ",
    " ___/ /  __/ |/ /  __/ / / /  / ___ |/ / / / /_/ /  / __  / /_/ / / __/   ",
    "/____/\\___/|___/\\___/_/ /_/  /_/  |_/_/ /_/\\__,_/  /_/ /_/\\__,_/_/_/     "
)
education_center = (
    " ______     _                   _______                      _             _   _ _ _",
    "|  ____|   | |                 |__   __|                    | |           (_) (_) | |",
    "| |__   ___| |_ _____   _____     | | ___ _ __ _ __ __ _  __| | __ _ ___   _   _| | | __ _",
    "|  __| / __| __/ _ \\ \\ / / _ \\    | |/ _ \\ '__| '__/ _` |/ _` |/ _` / __| | | | | | |/ _` |",
    "| |____\\__ \\ ||  __/\\ V /  __/    | |  __/ |  | | | (_| | (_| | (_| \\__ \\ | | | | | | (_| |",
    "|______|___/\\__\\___| \\_/ \\___|    |_|\\___|_|  |_|  \\__,_|\\__,_|\\__,_|___/ |_| |_|_|_|\\__,_|"
)

#Opciones
basic_options = ("Add/Remove/Show Players","Settings","Play Game","Ranking","Reports","Exit")

#Flags
flg_terminar = False
flg_00 = True

while not flg_terminar:

    while flg_00:
        opc = Create_Menus.make_menu(options=basic_options,title=title_game,space=200,symbol="*",distribution="A",secundary_symbol="=")
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
        else:
            flg_00 = False
            flg_terminar = True

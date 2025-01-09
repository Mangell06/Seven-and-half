#Archivo Base del video juego.

#Funciones importadas
import FUCTIONS.INTERFACE_FUCTIONS.Create_Menu as Create_Menus

opc = Create_Menus.make_menu(("1","2","3","4","5","6"),title="Hola_prueba",space=40,symbol="*")
if opc == 1:
    print(1)
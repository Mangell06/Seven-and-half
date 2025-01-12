def menuopciones(texto_opcion="",introducir_opcion="",rango_lista=[],excepciones=[]):
    while True:
        if texto_opcion != "":
            print(texto_opcion)
        introducir_opcion = input("Option: ")
        if introducir_opcion in excepciones:
            print("La opcion {} no esta permitida.\nVuelva a intentarlo.".format(introducir_opcion))
        elif introducir_opcion in rango_lista:
            return introducir_opcion
        else:
            print("La opcion {} no esta permitida.\nVuelva a intentarlo.".format(introducir_opcion))
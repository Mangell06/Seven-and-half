def menuopciones(texto_opcion="",introducir_opcion="",rango_lista=[],excepciones=[]):
    while True:
        if texto_opcion != "":
            print(texto_opcion.center(50))
        introducir_opcion = input("Option: ".center(50))
        if introducir_opcion in excepciones:
            error = "La opcion " + introducir_opcion + " no esta permitida.\nVuelva a intentarlo."
            print(error.center(50))
        elif introducir_opcion in rango_lista:
            return introducir_opcion
        else:
            error = "La opcion " + introducir_opcion + " no esta permitida.\nVuelva a intentarlo."
            print(error.center(50))
        input("Press enter to continue")
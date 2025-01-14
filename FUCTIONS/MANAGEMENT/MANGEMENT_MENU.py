def menuopciones(texto_opcion="",introducir_opcion="",rango_lista=[],excepciones=[]):
    while True:
        if texto_opcion != "":
            print(texto_opcion.center(50))
        opc = input(introducir_opcion)
        if not opc.isdigit():
            print("Invalid Option".center(50,"-"))
        if opc in rango_lista or opc in excepciones:
            return opc
        else:
            print("Invalid Option".center(50,"-"))
        input("Press enter to continue")
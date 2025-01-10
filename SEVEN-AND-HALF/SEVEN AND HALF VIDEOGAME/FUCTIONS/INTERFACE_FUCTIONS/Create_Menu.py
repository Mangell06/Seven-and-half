#Funcion para crear menus.
def make_menu(options,title="",space=40,symbol="",distribution="Distinct",secundary_symbol=""):
    while True:
        print()
        if symbol != "" or title != "" or space <= 0:
            if type(title) == str:
                if distribution == "Distinct":
                    print("".center(space,symbol))
                    print(title.center(space))
                    print("".center(space,symbol))
                else:
                    print(title.center(space,symbol))
            else:
                if distribution == "Distinct":
                    for i in range(len(title)):
                        print(title[i].center(space,symbol))
                else:
                    print("".center(space,symbol))
                    for i in range(len(title)):
                        print(title[i].center(space))
                    print()
                    print("".center(space,symbol))
                    print()
        for i in range(len(options)):
            text = str(i+1) + ") " + options[i]
            print("".rjust(space//2-10) + text)
        opc = input("".rjust(space//2-10) + "Option: ")
        print()
        if not opc.isdigit():
            print("Invalid Option".center(space,secundary_symbol))
        elif not int(opc) in range(1,len(options)+1):
            print("Invalid Option".center(space,secundary_symbol))
        else:
            return int(opc)
        input("".rjust(space//2-10) + "Press enter to continue")
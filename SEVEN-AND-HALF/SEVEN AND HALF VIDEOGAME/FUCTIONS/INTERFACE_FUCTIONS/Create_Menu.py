#Funcion para crear menus.
def make_menu(options,title="",space=40,symbol="",distribution="Distinct"):
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
                print("".center(space,symbol))
                for i in range(len(title)):
                    print(title[i])
                print("".center(space,symbol))
        for i in range(len(options)):
            text = str(i+1) + ") " + options[i]
            print(text.center(space))
        opc = input("Option: ".rjust(space//2+5))
        if not opc.isdigit():
            print("\nThe option is can only digit.")
        elif not int(opc) in range(1,len(options)+1):
            print("\nThe option out of range.")
        else:
            return opc
        input("\nEnter to continue")
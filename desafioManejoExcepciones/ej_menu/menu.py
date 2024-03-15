class Menu:
    
    def __init__(self):
        self.opciones = ["Opción 1", "Opción 2", "Opción 3", "Salir"]

    def menu(self):

        print(" *** MENU *** :")
        for i, opcion in enumerate(self.opciones, start=1):
            print(f"{i}. {opcion}")

    def opcion(self):
        opcion = input("Por favor, seleccione una opción: ")
        return opcion


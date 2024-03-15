from menu import Menu

if __name__ == "__main__":
    menu_instancia = Menu()

    while True:
        menu_instancia.menu()
        opcion_elegida = menu_instancia.opcion()

        #
        # try:
        #     opcion_elegida = int(opcion_elegida)
        #     if 1 <= opcion_elegida <= len(menu_instancia.opciones):
        #         print(f"Ha seleccionado: {menu_instancia.opciones[opcion_elegida - 1]}")
        #         if opcion_elegida == len(menu_instancia.opciones):
        #             print("Saliendo del programa...")
        #             break
        #     else:
        #         print("Opción no válida. Por favor, seleccione una opción válida.")
        # except ValueError:
        #     print("Por favor, ingrese un número válido.")
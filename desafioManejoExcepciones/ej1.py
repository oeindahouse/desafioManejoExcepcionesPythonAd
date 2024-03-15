class MiException(Exception):
    def __str__(self) -> str:
        detalle = self.args[0]
        return detalle["codigo"] + ": " + detalle["descripcion"]
    
    
    
    #2 def __init__(self, *args: object) -> None:
    #     super().__init__(*args)
    
    #1 def __init__(self, codigo,descripcion) -> None:
    #     self.codigo = codigo
    #     self.descripcion = descripcion

def validar_opcion(opcion):
    if opcion not in [1,2,3]:
        raise MiException({"codigo":"01","descripcion":"la opcion es invalida... "})

opcion=0

while opcion not in [1,2,3]:
    print('''
        1.- Opcion 1
        2.- Opcion 2
        3.- Opcion 3
        ''')
    try:
        
        #mi_dic = {"clave":"hola"}
        #mi_saludo = mi_dic["clavo"]
        opcion = int(input("Ingrese una opcion: "))
        validar_opcion(opcion)
        #a= 1 / 0
        if opcion not in [1,2,3]:
            raise MiException
        #else:
            #raise ValueError
    except ValueError as e:
        print("opcion invalida... ", e)
    except ZeroDivisionError as e:
        print("no se divide por cero... ", e)
        break
    except KeyError as e:
        print("la clave no existe en el dict...", e)
        break
    except MiException as e:
        print(e)
    except Exception as e:
        print("se ha producido una excepcion... ", e)
        break
    else:
        print("no habia excepcion o error")
    finally:
        print("siempre se ejecuta")
    
from error import DimensionError
from apoyo_desafio import Foto

foto = Foto(1,1 , (...))
print("ejemplo foto")

try:
    foto.ancho = 2500 #input("favor ingrese un ancho")
except DimensionError as e:
    print("error en el ancho: ", e)
    
try:
    foto.alto = 25000 #input("favor ingrese un alto") 
except DimensionError as e:
    print("error ene l alto: ", e)
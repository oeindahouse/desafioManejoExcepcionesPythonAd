from error import DimensionError

class Foto():
    Max = 2500
    Min = 1

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        self.ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho: int ) -> None:
        if ancho < self.Min or ancho > self.Max:
            raise DimensionError("min < ancho < max",ancho , self.Max)
        self.__ancho = ancho

    @property
    def alto(self) -> int :
        return self.__alto

    @alto.setter
    def alto(self, alto: int ) -> None:
        if alto < self.Min or alto > self.Max:
            raise DimensionError("min < alto < max" ,alto , self.Max)
        self.__alto = alto

class DimensionError(Exception):
    def __init__(self, mensaje='corrija el error... ', dimension=None, maximo=None):
        super().__init__(mensaje)
        self.dimension = dimension
        self.maximo = maximo


    def __str__(self):
        if self.dimension is not None and self.maximo is not None:
            return f"DimensionError: {self.args[0]}, su dimension: {self.dimension}, el maximo: {self.maximo}"
        return super().__str__()
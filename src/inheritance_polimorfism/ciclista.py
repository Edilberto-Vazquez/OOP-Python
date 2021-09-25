from src.inheritance_polimorfism.persona import Persona


class Ciclista(Persona):

    def __init__(self, nombre) -> None:
        super().__init__(nombre)

    def avanza(self):
        print('Me muevo en bicicleta')

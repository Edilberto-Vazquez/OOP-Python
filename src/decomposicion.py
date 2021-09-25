from src.motor import Motor
from src.llantas import Llantas
from src.estereo import Estereo


class Automovil:

    def __init__(self, modelo, marca, color) -> None:
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.__estado = 'en_reposo'
        self.__motor = Motor(cilindros=8)
        self.__llantas = Llantas(marca="continental", tamaño=15)
        self.__estereo = Estereo(marca="sony")

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self.__motor.inyecta_gasolina(10)
        else:
            self.__motor.inyecta_gasolina(3)
        self._estado = 'en_movimiento'

    def prenderEstereo(self, estado):
        self.__estereo.estado = estado

class Motor:

    def __init__(self, cilindros, tipo='gasolina') -> None:
        self.cilindros = cilindros
        self.tipo = tipo
        self.__temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass

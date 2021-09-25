class Lavadora:

    def __init__(self) -> None:
        pass

    def __llenar_tanque_agua(self, temperatura):
        print(f'Llenado el tanque con agua {temperatura}')

    def __anadir_jabon(self):
        print('añadiendo jabón')

    def __lavar(self):
        print("Lavando la ropa")

    def __centrifugar(self):
        print('Centrifugando la ropa')

    def lavar(self, temperatura='caliente'):
        self.__llenar_tanque_agua(temperatura)
        self.__anadir_jabon()
        self.__lavar()
        self.__centrifugar()

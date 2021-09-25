class CasillaVotacion:

    def __init__(self, identificador, pais) -> None:
        self.__identrifiador = identificador
        self.__pais = pais
        self.__region = None

    # ---Without @property decorator---
    # def get_region(self):
    #     return self.__region

    # def set_region(self, region):
    #     if region in self.__pais:
    #         self.__region = region
    #     else:
    #         raise ValueError(
    #             f'La region {region} no esta en el pais {self.__pais}')

    # ---With @property decorator---
    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(
                f'La region {region} no esta en el pais {self.__pais}')

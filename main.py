from src.coordenada import Coordenada
from src.decomposicion import Automovil


def main():
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    # print(coord_1.distancia(coord_2))
    print(isinstance(coord_2, Coordenada))

    # Decomposicion
    auto_1 = Automovil("ford", "Spark", "Azul chiclamino")
    auto_1.prenderEstereo(True)
    print(auto_1)


if __name__ == '__main__':
    main()

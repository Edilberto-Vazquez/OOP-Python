from src.coordenada import Coordenada
from src.decomposicion.decomposicion import Automovil
from src.abstraccion.abstraccion import Lavadora
from src.decorators.casilla_votacion import CasillaVotacion
from src.inheritance_polimorfism.persona import Persona
from src.inheritance_polimorfism.ciclista import Ciclista


def main():
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    # print(coord_1.distancia(coord_2))
    # print(isinstance(coord_2, Coordenada))

    # Decomposicion
    # auto_1 = Automovil("ford", "Spark", "Azul chiclamino")
    # auto_1.prenderEstereo(True)
    # print(auto_1)

    # Abstraccion
    # lavadora = Lavadora()
    # lavadora.lavar()

    # encapsulacion, getters y setters con @property decorator
    # casilla = CasillaVotacion(
    #     3254684, ['Tlaxcala', 'Veracruz', 'Monterrey', 'Ciudad de Mexico'])
    # casilla.region = 'Veracruz'
    # print(casilla.region)

    # Herencia Polimorfismo
    # persona = Persona('Edilberto')
    # ciclista = Ciclista('Maria')
    # persona.avanza()
    # ciclista.avanza()


if __name__ == '__main__':
    main()

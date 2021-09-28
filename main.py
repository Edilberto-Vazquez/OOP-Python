from src.coordenada import Coordenada
from src.decomposicion.decomposicion import Automovil
from src.abstraccion.abstraccion import Lavadora
from src.decorators.casilla_votacion import CasillaVotacion
from src.inheritance_polimorfism.persona import Persona
from src.inheritance_polimorfism.ciclista import Ciclista
from src.complejidad_algoritmica import factorial, factorial_r
import time
import sys
from src.linear_search import busqueda_lineal
from src.binary_seacrh import busqueda_binaria
from src.bubble_sort import ordenamiento_burbuja
import random


def main():
    # coord_1 = Coordenada(3, 30)
    # coord_2 = Coordenada(4, 8)

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

    # complejidad algoritmica
    # sys.setrecursionlimit(100010)
    # sys.setrecursionlimit(200000)
    # n = 100000
    # comienzo = time.time()
    # factorial(n)
    # final = time.time()
    # print(final - comienzo)

    # comienzo = time.time()
    # factorial_r(n)
    # final = time.time()
    # print(final - comienzo)

    # Busqueda lineal
    # tamaño_lista = int(input('De que tamaño sera la lista?'))
    # objetivo = int(input('Que numero quieres encontrar?'))

    # lista = [random.randint(0, 100) for i in range(tamaño_lista)]
    # encontrado = busqueda_lineal(lista, objetivo)
    # print(lista)
    # print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"}')

    # Busqueda binaria
    # tamaño_lista = int(input('De que tamaño sera la lista?'))
    # objetivo = int(input('Que numero quieres encontrar?'))

    # lista = sorted([random.randint(0, 100) for i in range(tamaño_lista)])
    # encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    # print(lista)
    # print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"}')

    # Bubble sort (ordenamiento burbuja)
    tamaño_lista = int(input('De que tamaño sera la lista?'))

    lista = [random.randint(0, 100) for i in range(tamaño_lista)]
    print(lista)
    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)


if __name__ == '__main__':
    main()

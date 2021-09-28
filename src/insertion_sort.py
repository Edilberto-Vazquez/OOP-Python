import random


def ordenamiento_insercion(lista):
    desordenada = lista
    ordenada = []
    valor_actual = lista[1]

    for value in range(1, len(lista)-1):
        valor_actual = lista[value]
        indice_actual = value

        while indice_actual > 0 and lista[indice_actual - 1] > valor_actual:
            lista[indice_actual] = lista[indice_actual-1]
            indice_actual -= 1
        lista[indice_actual] = valor_actual
    return lista


if __name__ == '__main__':
    tamaño_lista = int(input('De que tamaño sera la lista?'))
    lista = [random.randint(0, 100) for i in range(tamaño_lista)]
    print(lista)
    lista_ordenada = ordenamiento_insercion(lista)
    print(lista_ordenada)

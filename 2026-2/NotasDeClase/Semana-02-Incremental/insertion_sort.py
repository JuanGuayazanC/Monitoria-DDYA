##
# Encuentra la posición en la que debe insertarse un elemento para mantener
# una lista ordenada de forma ascendente.
#
# @param arr Lista ordenada en la que se buscará la posición.
# @param ele Elemento que se desea insertar.
# @return Índice en el que debe insertarse el elemento.
#
def findElementIndex(arr, ele):
    index = 0

    while index < len(arr) and arr[index] < ele:
        index += 1

    return index


##
# Inserta un elemento en la posición correspondiente dentro de una lista
# previamente ordenada.
#
# Esta función crea una nueva lista y no modifica directamente la lista
# recibida.
#
# @param arr Lista ordenada en la que se insertará el elemento.
# @param ele Elemento que se desea insertar.
# @return Nueva lista ordenada que contiene el elemento insertado.
#
def sortedSlice(arr, ele):
    index = findElementIndex(arr, ele)

    return arr[:index] + [ele] + arr[index:]


##
# Ordena una lista de forma ascendente mediante el algoritmo de ordenamiento
# por inserción (Insertion Sort).
#
# En cada fase, el algoritmo toma un elemento de la parte no ordenada y lo
# inserta en la posición apropiada dentro de la parte que ya está ordenada.
# Durante el proceso se imprimen los resultados parciales de cada fase.
#
# @param arr Lista de elementos comparables que se desea ordenar.
# @return Lista con los elementos ordenados de forma ascendente.
#
def insertionSort(arr):
    if len(arr) <= 1:
        return arr

    for index in range(1, len(arr)):
        print("Fase {} : {} <-- {}".format(
            index,
            arr[:index],
            arr[index]
        ))

        sorted_part = sortedSlice(arr[:index], arr[index])
        print("Resultado de la fase:", sorted_part)

        arr = sorted_part + arr[index + 1:]
        print("Resultado total:", arr)

    return arr

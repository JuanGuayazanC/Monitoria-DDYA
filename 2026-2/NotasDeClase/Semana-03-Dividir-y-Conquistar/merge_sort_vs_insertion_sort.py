from random import randint
from time import time


##
# Combina dos listas ordenadas de forma ascendente en una sola lista ordenada.
#
# @param left Lista ordenada.
# @param right Lista ordenada.
# @return Lista resultante de combinar ambas listas de forma ordenada.
#
def merge(left, right):
    index_left, index_right, result = 0, 0, []
    while index_left < len(left) and index_right < len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
    if index_left < len(left):  # Quedan elementos en left
        result += left[index_left:]
    else:  # Quedan elementos en right
        result += right[index_right:]
    return result


##
# Ordena una lista de forma ascendente mediante el algoritmo Merge Sort
# (dividir y conquistar). Complejidad O(n log n).
#
# @param L Lista de elementos comparables que se desea ordenar.
# @return Lista con los elementos ordenados de forma ascendente.
#
def mergeSort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    resultLeft, resultRight = mergeSort(L[:mid]), mergeSort(L[mid:])
    result = merge(resultLeft, resultRight)
    return result


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
# por inserción (Insertion Sort). Complejidad O(n^2).
#
# @param arr Lista de elementos comparables que se desea ordenar.
# @return Lista con los elementos ordenados de forma ascendente.
#
def insertionSort(arr):
    if len(arr) <= 1:
        return arr

    for index in range(1, len(arr)):
        sorted_part = sortedSlice(arr[:index], arr[index])
        arr = sorted_part + arr[index + 1:]

    return arr


##
# Compara el tiempo de ejecución de Insertion Sort y Merge Sort sobre
# listas aleatorias de distintos tamaños.
#
def main():
    sizes = [512, 1024, 2048, 10000]
    for lm in sizes:
        arr = [randint(0, int(1e6)) for _ in range(lm)]

        t0 = time()
        print(insertionSort(arr))
        t1 = time()
        print("Insertion Sort time {}".format(t1 - t0))

        t0 = time()
        print(mergeSort(arr))
        t1 = time()
        print("Merge Sort time {}".format(t1 - t0))


main()

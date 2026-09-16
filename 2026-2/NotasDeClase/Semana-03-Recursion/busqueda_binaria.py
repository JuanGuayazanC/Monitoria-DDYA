##
# Busca un elemento en un arreglo ordenado mediante búsqueda binaria
# recursiva. Complejidad O(log n).
#
# @param arreglo Arreglo ordenado de forma ascendente en el que se busca.
# @param elemento Elemento que se desea encontrar.
# @return True si el elemento está en el arreglo, False en caso contrario.
#
def busquedaBinaria(arreglo, elemento):
    if len(arreglo) == 0:
        return False
    if len(arreglo) == 1 and arreglo[0] != elemento:
        return False

    mid = len(arreglo) // 2

    if arreglo[mid] == elemento:
        return True

    if arreglo[mid] < elemento:
        return busquedaBinaria(arreglo[mid + 1:], elemento)

    return busquedaBinaria(arreglo[:mid], elemento)

##
# Ordena una lista de forma ascendente mediante el algoritmo de ordenamiento
# por selección (Selection Sort), implementado de forma recursiva.
#
# En cada llamada se extrae el mínimo de la lista restante y se añade a la
# respuesta acumulada hasta agotar los elementos.
#
# @param lista Lista de elementos comparables aún sin ordenar.
# @param respuesta Lista acumulada con los elementos ya ordenados.
# @return Lista con los elementos ordenados de forma ascendente.
#
def ordenar(lista, respuesta):
    print(lista, respuesta)
    if len(lista) <= 1:
        return respuesta + lista
    mn = min(lista)
    lista.remove(mn)
    return ordenar(lista, respuesta + [mn])


print(ordenar([-5, 1, 2, 3], []))

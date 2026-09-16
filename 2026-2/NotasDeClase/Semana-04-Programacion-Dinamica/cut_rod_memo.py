import math

MEM = {}

LONG = 0
GANANCIA = 1


##
# Calcula la máxima ganancia posible al cortar una vara de longitud l,
# de forma recursiva sin memoización, dada una configuración de cortes
# disponibles (longitud, ganancia).
#
# @param l Longitud de la vara disponible.
# @param config Lista de tuplas (longitud, ganancia) de cortes posibles.
# @return Máxima ganancia alcanzable.
#
def cutRod(l, config):
    if l < min(config)[LONG]:
        return 0
    mx = -math.inf
    for corte in config:
        c_long, c_ganancia = corte
        if c_long <= l:  # Corte posible
            mx = max(mx, cutRod(l - c_long, config) + c_ganancia)
    return mx


##
# Fase de cómputo de Cut Rod con memoización: calcula el resultado
# apoyándose en cutRodM para las llamadas recursivas.
#
# @param l Longitud de la vara disponible.
# @param config Lista de tuplas (longitud, ganancia) de cortes posibles.
# @param M Tabla de memoización.
# @return Máxima ganancia alcanzable.
#
def cutRodP(l, config, M):
    if l < min(config)[LONG]:
        return 0
    mx = -math.inf
    for corte in config:
        c_long, c_ganancia = corte
        if c_long <= l:  # Corte posible
            mx = max(mx, cutRodM(l - c_long, config, M) + c_ganancia)
    return mx


##
# Calcula la máxima ganancia posible al cortar una vara de longitud l,
# de forma recursiva con memoización.
#
# @param l Longitud de la vara disponible.
# @param config Lista de tuplas (longitud, ganancia) de cortes posibles.
# @param M Tabla de memoización, indexada por (l, str(config)).
# @return Máxima ganancia alcanzable.
#
def cutRodM(l, config, M):
    key = (l, str(config))
    if key in M.keys():
        return M[key]
    M[key] = cutRodP(l, config, M)
    return M[key]


def main():
    conf = [(3, 1.0), (5, 3.0), (10, 8.0), (1, 10.0)]
    print(cutRodM(100, conf, MEM))

    conf = [(3, 50.0), (5, 3.0), (10, 8.0), (1, 10.0)]
    print(cutRodM(100, conf, MEM))

    print(MEM)


main()

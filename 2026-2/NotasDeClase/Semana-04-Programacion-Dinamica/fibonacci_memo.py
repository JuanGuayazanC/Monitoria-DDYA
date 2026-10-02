M = [None for i in range(int(1e5))]


##
# Calcula el n-ésimo número de Fibonacci de forma recursiva, sin memoización.
# Complejidad exponencial O(2^n).
#
# @param n Índice del número de Fibonacci a calcular.
# @return El n-ésimo número de Fibonacci.
#
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


##
# Fase de cómputo de Fibonacci con memoización: calcula el resultado
# apoyándose en fiboM para las llamadas recursivas.
#
# @param n Índice del número de Fibonacci a calcular.
# @param M Tabla de memoización.
# @return El n-ésimo número de Fibonacci.
#
def fiboP(n, M):
    if n <= 1:
        return n
    return fiboM(n - 1, M) + fiboM(n - 2, M)


##
# Calcula el n-ésimo número de Fibonacci de forma recursiva con
# memoización. Complejidad O(n).
#
# @param n Índice del número de Fibonacci a calcular.
# @param M Tabla de memoización.
# @return El n-ésimo número de Fibonacci.
#
def fiboM(n, M):
    if M[n] is not None:
        return M[n]
    M[n] = fiboP(n, M)
    return M[n]


def main():
    n = int(1e3)
    for i in range(n):
        fiboM(i, M)
    print(fiboM(n, M))


main()

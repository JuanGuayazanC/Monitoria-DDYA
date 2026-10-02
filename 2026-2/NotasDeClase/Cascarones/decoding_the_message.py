from sys import stdin


##
# Procesa un renglón del mensaje cifrado y devuelve el mensaje decodificado.
#
# Cascarón de entrada/salida para el problema de arena "Decoding the
# Message"; la lógica de decodificación queda pendiente de implementar.
#
# @param line Renglón de texto a procesar.
# @return Mensaje decodificado correspondiente al renglón.
#
def procesarRenglon(line):
    palabras = line.split()
    mensaje = ""
    return mensaje


def main():
    n_parrafos = int(stdin.readline().strip())
    linea_vacia = stdin.readline().strip()
    for i in range(0, n_parrafos):
        print("Case #{}:".format(i + 1))
        renglon = stdin.readline().strip()
        while renglon:
            print(procesarRenglon(renglon))
            renglon = stdin.readline().strip()
        print("")


main()

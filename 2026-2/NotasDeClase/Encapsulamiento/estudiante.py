from uuid import uuid1
from random import randint


class Estudiante:

    def __init__(self, nombre, id):
        # Seccion de declaracion de atributos
        self.nombre = ""
        self.id = None
        self.notas = {}
        self.gpa = 0.0
        # Seccion de asignación de atributos
        self.setNombre(nombre)
        self.setId(id)

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        if not isinstance(nombre, str):
            raise Exception("El nombre no corresponde al tipo de dato esperado")
        self.nombre = nombre

    def getId(self):
        return self.id

    def setId(self, id):
        if not (isinstance(id, int) or id is None):
            raise Exception("El id no corresponde al tipo de dato esperado")
        self.id = id

    def getNotas(self):
        return self.notas

    def añadirNota(self, nota):
        self.notas[nota[0]] = nota[1]
        self.calcularGPA()

    def calcularGPA(self):
        totalNotas = len(self.notas.keys())
        if totalNotas > 0:
            self.gpa = sum(self.notas.values()) / totalNotas

    def __str__(self):
        return "Estudiante({}, {}, {}, {})".format(self.id, self.nombre, self.notas, self.gpa)


def main():
    estudiantes = [Estudiante(str(uuid1()), randint(0, int(1e6))) for i in range(10)]
    for e in estudiantes:
        notas = [(str(uuid1()), randint(15, 50) / 10) for i in range(3)]
        for nota in notas:
            e.añadirNota(nota)
    for e in estudiantes:
        print(e)


main()

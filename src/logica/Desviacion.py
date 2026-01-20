import math


class Desviacion:
    def __init__(self, datos):
        self.__datos = datos


    def calcular(self):
        n = len(self.__datos)

        if n == 0:
            return None
        if n == 1:
            return 0

        promedio = sum(self.__datos) / n
        varianza = sum((x - promedio) ** 2 for x in self.__datos) / n
        return math.sqrt(varianza)
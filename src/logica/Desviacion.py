# src/logica/Desviacion.py
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
        suma = 0
        for x in self.__datos:
            suma += (x - promedio) ** 2

        return math.sqrt(suma / n)
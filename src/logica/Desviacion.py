# src/logica/Desviacion.py
class Desviacion:
    def __init__(self, datos):
        self.__datos = datos

    def calcular(self):
        if len(self.__datos) == 0:
            return None

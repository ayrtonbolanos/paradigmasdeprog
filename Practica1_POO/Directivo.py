from typing import DefaultDict
from Persona.Persona import Persona


class Directivo(Persona):
    """Clase Empleado Tipo Persona"""

    def __init__(self, nombre, edad, categoria):
        Persona.__init__(self, nombre, edad)
        self.categoria #Nuevos atributos

    def mostrar(self):
        #Método que devuelve cadena de Empleado
        return self.nombre, self.edad, self.categoria
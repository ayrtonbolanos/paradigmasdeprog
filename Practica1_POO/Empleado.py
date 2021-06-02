from typing import DefaultDict
from Persona.Persona import Persona


class Empleado(Persona):
    """Clase Empleado Tipo Persona"""

    def __init__(self, nombre, edad, sueldo_bruto):
        Persona.__init__(self, nombre, edad)
        self.sueldo_bruto #Nuevos atributos

    def sueldo_bruto(self):
        return self.sueldo_bruto

    def mostrar(self):
        #Método que devuelve cadena de Empleado
        return self.nombre, self.edad, Empleado.sueldo_bruto
    

    

        
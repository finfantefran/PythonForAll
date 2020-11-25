'''
Created on 28 oct. 2020

@author: finfatefran
'''

"""Impedir acceso a determinados metodos o atributos desde fuera de la clase"""

# Una varible privada o metodo empieza con __variable
# Esto no hace a la variable o metodo realmente privados, sino que se puede acceder mecdiante el nombre de la clase objeto._NombreClase__privado()


class Ejemplo:
    def publico(self):
        print "Publico"
    
    def __privado(self):
        print "Privado"

ej=Ejemplo()
ej.publico()

# ej.__privado() MAL
ej._Ejemplo__privado()

# Getters y Setters para acceder a variables
class Fecha():
    def __init__(self):
        self.__dia=1
    
    def getDia(self):
        return self.__dia
    
    def setDia(self,dia):
        self.__dia=dia
        
# Tambien se puede utilizar propery para modificar valores del atributo protegido
class Fecha2():
    def __init__(self):
        self.__dia=1
    
    def getDia(self):
        return self.__dia
    
    def setDia(self,dia):
        self.__dia=dia
        
    dia = property(getDia,setDia)

mi__fecha=Fecha2()
mi__fecha.dia=33

        
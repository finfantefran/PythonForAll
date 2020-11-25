'''
Created on 28 oct. 2020

@author: finfantefran
'''

"""Devolver una funcion en base a un param de entrada"""


def saludar(lang):

    def saludar_es():
        print "Hola"
    
    def saludar_en():
        print "Hi"
    
    def saludar_fr():
        print "Salut"

    lang_func = {"es":saludar_es,
               "en":saludar_en,
               "fr":saludar_fr}
    print(lang_func.keys())

    return lang_func[lang]


# Devuelve la funcion saludar_es()
f = saludar("es")
f()

saludar("en")()

"""Iteraciones de orden superior sobre listas"""
"""map"""


# map(function, sequence[]), aplica a una lista y sus elementos una funcion
def cuadrado(n):
    return n ** 2


l = [1, 2, 3]
l2 = map(cuadrado, l)
print l2

"""filter"""


# filter(function,sequence) verifica que los elementos de una lista cumplan una condicion
def par(n):
    return (n % 2.0 == 0)


l3 = filter(par, l)
print l3

"""Funciones Lambda"""
"""Son funciones anonimas que no pueden ser referenciadas, se construyen mediante
lambda paramEntrada: codigo de la funcion"""
l4 = filter(lambda n: n % 2.0 == 0, l)
print l4

"""Comprension de listas"""
l = [0, 1, 2, 3]
m = ["a", "b"]
n = [s * v for s in m
for v in l
if v > 0]
print n


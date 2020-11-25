'''
Created on 28 oct. 2020

@author: finfantefran
'''

"""Son como listas pero se declaran con parentesis, pero son INMUTABLES y gracias a ello LIGERAS,ahorran memoria"""

t=(1,2,True,"python",[1,3])
print t[-1]

# En realidad los parentesis no hacen falta, se construye con comas
t=1,2,3
print type(t)

# Para declarar una Tupla de un elemento, es necesario anhadir una coma
tp=1,
print type(t)

# Para acceder a elementos se utiliza [], igual que con listas
print t[1]

# Como las cadenas de caracteres son secuencias, tambien se puede hacer slicing o acceder a ellas como listas o tuplas
c="Hola mundo"
print c[0]
print c[5:]

'''
Created on 28 oct. 2020

@author: finfantefran
'''

"""Colecciones ordenadas (Array o vector)"""

# Se crea indicando entre corchetes y separados por comas sus valores, y puede contener otras listas
l=[22,True,"una lista",[1,2]]
# El indice inicial es 0
print l[3][1]
# Actualizar valor
l[0]=1
print l[0]

# Utilizando [-3] accedemos al antepenultimo valor
print l[-3]

# Utilizando [-2] accedemos al penultimo valor
print l[-2]

# Utilizando [-1] accedemos al ultimo valor
print l[-1]

# Podemos particionar la lista para coger porciones lista[inicio:fin]
print l[:-2]
print l[:-3]
print l[:]


"""Anadir objto al final de la lista"""
print l.append(1)

"""Devuelve el num de veces que esta ese valor en la lista"""
print l.count(1)

"""Anhade elementos del iterable a la lista"""
otraLista=["hola","hola"]
l.extend(otraLista)
print l


"""Devuelve la posicion en la que se encontro la primera ocurrencia de l valor buscado, se puede especificar un inicio y fin de busqueda"""
print l.index("hola")

"""Inserta un objeto en una posicionsin eliminar el que ya existe si se escogiera una ocupada """
l.insert(2, "object")
print l


"""Eliminar el primer valor que coincida"""
l.remove("object")
print l

"""Obtener valor y eliminar el objeto que hay en una posicion, si no se le especifica elimina el ultimo"""
print l.pop(0)

"""Ordenar una lista lista.sort(cmp=None, key=None, reverse= False)"""
l.sort(cmp=None, key=None, reverse=False)
print l
l.sort(cmp=None, key=None, reverse=True)
print l











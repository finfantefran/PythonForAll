'''
Created on 28 oct. 2020

@author: finfantefran
'''

"""Colecciones que relacionan clave:valor"""

d={"Love Actually":"Richard Curtis","Kill Bill":"Tarantino"}

# Las claves son valores inmutables, y se puede utiizar cualquier valor excepto listas o diccionarios.
# Un diccionario es una tabla hash, y esta hash no se puedemodificar si ya se ha calculado para una clave

# Para acceder a un valor se utiliza la clave entre corchetes diccionario[clave]
print d["Love Actually"]

# Para reasignar valores igual
d["Love Actually"]="Hiuhg Grant"
print d["Love Actually"]

# Los diccionarios son mappings (mapeados) y no secuencias



"""Buscar valor en un diccionario utilizando el metodo de modo que podamos 
devolver un valor si no se encuentra la clave"""

print d.get("Love Actuallys", "no existe")


"""Comprobar si existe una clave determinada"""
print d.has_key("Love Actually")

"""Lista de tuplas con los pares clave-valor"""
print d.items()

"""Lista con las keys"""
print d.keys()

"""Borra la clave y devuelve su valor"""
print d.pop("Love Actually")

"""Lista de valores"""
print d.values()





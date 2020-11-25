'''
Created on 28 oct. 2020

@author: finfantefran
'''

s="Hola que tal estas mundo."


"""Num de veces que se encuantra la subcadena en la cadena s.count(sub[,start[,end]])"""
print s.count("H")
print s.count("e",0,-1)

"""Posicion en la que se encontro porprimera vez el caracter o subcadena en la cadena"""
print s.find("H")
sequence="Muy bien."
# print s.join(sequence)
"""Busca el separador y devuelbe una tupla hasta dicho separador"""
print s.partition(" ")

"""Devuelve una lista con las subcadenas en las que se divide la cadena por el delimitador especificado"""
print s.split(" ")
print s.split(" ",1) # se le puede especificar que solo lo busque una vez



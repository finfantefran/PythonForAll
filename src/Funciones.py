'''
Created on 28 oct. 2020

@author: finfantefran
'''



def mi_funcion(param1, param2):
    """Docstring: documentar la funcion"""
    print param1
    print param2
    


# Llamada a la funcion sin modificar orden de params
mi_funcion("hola", 1)

# Llamada a la funcion modificando orden params
mi_funcion(param2=1, param1="adios")

# Valores por defecto al definir la funcion en caso de que no se especifiquen al llamarla
def imprimir(texto,veces=1):
    print veces*texto

imprimir("h")
imprimir("h",5)

# Definir funcion con un numero varibale de argumentos, *otros crea una tupla con los params anhadidos
def varios(param1,param2,*otros):
    for val in otros:
        print val

varios(1,2,3,4)


# Se puede definir otros como **otros, de esta manera en vez de una tupla, se crea un diccionarios con los valores asociados a los nombres de variables

def varios2(param1,param2,**otros):
    for i in otros.items():
        print i
varios2(1,2,tercero=3)



# El paso de variables por referencia se refiere a un puntero, apunta a la direccion de memoria de otra varibale
# El paso de varibale por valor tiene distinto espacio de memoria
# En Python se utiliza el paso por valor a las funciones




"""Cuando pasamos una varible inmutable a una funcion aunque no sea global si se modifica dentro de la funcion permanece igual fuera,
pero si esta esmutable cambio, como una lista"""

def f(x,z):
    x=x+3
    z.append(23)
    print x,z
x=22
y=[22]

f(x,y)
print x,y

# Valores mutables serian como punteros, los inmutables como paso por valor

# Para devolver varios valores en una funcion, python crea una tuplapor defecto, sino pues podemos devolver un valor, un diccionario, una lista ...
def f2(x,y):
    return x*2,y*2
print f2(2,1)








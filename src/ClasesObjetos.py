'''
Created on 28 oct. 2020

@author: finfantefran
'''




class Coche:
    """DocString"""
    def __init__(self,gasolina):
        self.gasolina=gasolina
        print "init: ",gasolina
        
    def arrancar(self):
        print "arrancar",self.gasolina

# self. para crear un atributo de clase golbal, del objeto o un metodo de clase


    

# crear objeto de clase, el parametro self se pasa automaticamente

mi_coche=Coche(3)

mi_coche.arrancar()











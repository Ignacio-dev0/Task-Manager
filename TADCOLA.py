#TAD COLA
from TADTAREA import *
#Colores para texto
RED = '\033[31m' 
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
RESET = '\033[0m' #Sirve para cortar el color

def crearCola():
    #Crea una cola vacia 
    cola=[]
    return cola

def esVacia(cola):
    #Retorna verdadero si la pila no tiene elementos
    return len(cola)==0

def encolar(cola,elem):
    #Agrega un elemento al final de la cola
    cola.append(elem)

def desencolar(cola):
    #Retorna y elimina el primer elemento de la cola
    elem=cola.pop(0)
    return elem

def tamanioCola(cola):
   #Retorna la cantidad de elementos de la cola
   return len(cola)

def copiarCola(cola1,cola2):
   #Copia cola 2 en 1
   aux=crearCola() 
   while not esVacia(cola2):
        elem=desencolar(cola2)
        encolar(aux,elem) 
   while not esVacia(aux):
        elem=desencolar(aux)
        encolar(cola1,elem)
        encolar(cola2,elem)


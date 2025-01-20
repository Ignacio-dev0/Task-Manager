#tad tareas
from TADTAREA import *
#Colores para texto
RED = '\033[31m' 
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
RESET = '\033[0m' #Sirve para cortar el color

def crearLista():
    #Crea una lista de tareas
    lista=[]
    return lista

def agregarTarea(lista,t):
    #Agrega una tarea a la lista
    lista.append(t)

def eliminarTarea(lista,t):
    #Elimina una tarea de la lista
    lista.remove(t)

def recuperarTarea(lista,i):
    #Recupera la tarea de la iesima posicion
    return lista[i-1]

def tamanio(lista):
    #Retorna la cantidad de tareas de la lista
    return len(lista)

def existeTarea(lista,t):
    #Retorna True o False si la tarea se encuentra en la lista o no
    return t in lista


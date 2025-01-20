#TAD TAREA
#Importacion de libreria datetime
import datetime as d 
from datetime import *

#nombre, descripción, asignado(Quien hace la tarea), estado (pendiente, en progreso, completada) 
#y fecha de vencimiento
def crearTarea():
    #Se crea una tarea vacia
    tarea=["","","","",0]  
    return tarea

def cargarTarea(t,nom,desc,asig,estado,dia,mes,anio):
    #Carga el nombre,descripcion,asignado,estado,fecha de vencimiento en t
    t[0]=nom
    t[1]=desc
    t[2]=asig
    t[3]=estado
    fechaVenc= d.datetime(anio,mes,dia)
    t[4]=fechaVenc

def verNom(t):
    #Retorna el nombre de la tarea
    return t[0]

def verDesc(t):
    #Retorna la descripcion de la tarea
    return t[1]

def verAsig(t):
    #Retorna si esta asignado o no la tarea
    return t[2]

def verEstado(t):
    #Retorna el estado de la tarea
    return t[3]

def verFecha(t):
    #Retorna la fecha de vencimiento de la tarea
    return t[4].date()


def modNom(t,nom):
    #Modifica el nombre de la tarea
    t[0]=nom

def modDesc(t,desc):
    #Modifica la descripcion de la tarea
    t[1]=desc

def modAsig(t,asig):
    #Modifica si la tarea esta asignada o no
    t[2]=asig

def modEstado(t,estado):
    #Modifica el estado de la tarea
    t[3]=estado

def modFecha(t,dia,mes,anio):
    #Modifica la fecha de vencimiento de la tarea
    fecha=d.datetime(anio,mes,dia)
    t[4]=fecha


def copiar(t1,t2):
    #Copia lo que esta en t2 y lo pega en t1
    t1[0]=t2[0]
    t1[1]=t2[1]
    t1[2]=t2[2]
    t1[3]=t2[3]
    t1[4]=t2[4]
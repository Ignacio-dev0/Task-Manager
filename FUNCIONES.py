from TADTAREA import *
from TADCOLA import *
from TADTAREAS import *

def eliminarTarea_Cola(cola1, elem1):
    #Elimina la tarea en la cola 
    aux=crearCola() 
    while not esVacia(cola1):
        elem=desencolar(cola1)
        if elem!=elem1:
            encolar(aux,elem) 
    while not esVacia(aux):
        elem=desencolar(aux)
        encolar(cola1,elem)

def imprimirCola(cola):
    colaAux=crearCola()
    print("Tareas en progreso:")
    copiarCola(colaAux, cola) #Creo una auxiliar
    print(f'{MAGENTA}{"Nombre" : <15}{"Descripcion" : <25}{"Asignado" : <15}{"Estado" : <15}{"Fecha de vencimiento"}{RESET}')
    while not esVacia(colaAux): #Mientras la cola no este vacia, desencolo e imprimo cada propiedad de la tarea
        tarea = desencolar(colaAux)
        
        print(f"{verNom(tarea) : <15}{verDesc(tarea) : <25}{verAsig(tarea) : <15}{YELLOW}{verEstado(tarea) : <15}{RESET}{verFecha(tarea)}")

def imprimirTareas(lista):
    if tamanio(lista)==0: #Me aseguro si este vacio
                print("No hay tareas registradas.")
    else:
        print(f'{GREEN}{"Nombre" : <15}{"Descripcion" : <25}{"Asignado" : <15}{"Estado" : <15}{"Fecha de vencimiento"}{RESET}')
        for i in range(1,(tamanio(lista)+1)): #Imprimo cada detalle de cada tarea en la lista
            tarea=recuperarTarea(lista,i)
                    
            print(f"{verNom(tarea) : <15}{verDesc(tarea) : <25}{verAsig(tarea) : <15}{verEstado(tarea) : <15}{verFecha(tarea)}")
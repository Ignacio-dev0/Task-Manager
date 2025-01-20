#IMPORTO LAS LIBRERIAS NECESARIAS PARA LA APLICACION
from TADTAREA import *
from TADTAREAS import *
from TADCOLA import *
from FUNCIONES import *

import os
#Colores para texto
RED = '\033[31m' 
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
RESET = '\033[0m' #Sirve para cortar el color

print("Comenzó el programa")
lista=crearLista() #SE CREA LA LISTA DE TAREAS VACIA
cola=crearCola() #Creo cola vacia

#CARGA INICIAL
t=crearTarea() # se crea una nueva tarea
cargarTarea(t,'tarea1','desc1','Felix','pendiente',27,4,2024)
agregarTarea(lista,t)

t=crearTarea() # se crea una nueva tarea
cargarTarea(t,'tarea2','desc2','Felix','en progreso',5,2,2024)
agregarTarea(lista,t)
encolar(cola, t)

t=crearTarea() # se crea una nueva tarea
cargarTarea(t,'tarea3','desc3','Juan','completada',8,3,2024)
agregarTarea(lista,t)

t=crearTarea() # se crea una nueva tarea
cargarTarea(t,'tarea4','desc4','Juan','en progreso',10,4,2024)
encolar(cola, t)
agregarTarea(lista,t)

t=crearTarea() # se crea una nueva tarea
cargarTarea(t,'tarea5','desc5','Tomas','en progreso',1,1,2025)
agregarTarea(lista,t)
encolar(cola, t)

t=crearTarea() # se crea una nueva tarea
cargarTarea(t,'tarea6','desc6','Tomas','completada',20,11,2024)
agregarTarea(lista,t)

t=crearTarea() # se crea una nueva tarea
cargarTarea(t,'tarea7','desc7','Lautaro','en progreso',11,8,2024)
agregarTarea(lista,t)
encolar(cola, t)

t=crearTarea() # se crea una nueva tarea
cargarTarea(t,'tarea8','desc8','Lautaro','pendiente',2,7,2024)
agregarTarea(lista,t)

t=crearTarea() # se crea una nueva tarea
cargarTarea(t,'tarea9','desc9','Axel','en progreso',10,2,2024)
agregarTarea(lista,t)
encolar(cola, t)

del t


opc='f'
while opc!='z':
    print("\nSISTEMA DE GESTION DE PROYECTOS")
    print("\nMenu de opciones")
    print("================================================")
    print("Elegir una de las opciones")
    print("a.  Agregar tarea")
    print("b.  Modificar tarea")
    print("c.  Eliminar tarea")
    print("d.  Listar tareas") #Lista todas las tareas y sus detalles
    print("e.  Modificar fecha de vencimiento de tareas") #ENTRE DOS FECHAS DADAS
    print("f.  Generar reporte de las tareas") #POR ESTADO
    print("g.  Eliminar tareas asignadas a un empleado")
    print("h.  Listar tareas en Progreso") #Con cola
    print("z.  Salir del programa")
    print("================================================")

    
    
    opc=input("Ingrese una opción: ")
    opc=opc.lower() # .lower() para que no distinga entre minusculas y mayusculas

    os.system('cls' if os.name == 'nt' else 'clear') #Limpia la pantalla
    
    if (opc=='a'): #Dar de alta las tareas
        t=crearTarea() # se crea una nueva tarea
        print("Dar de alta una tarea:\n--------------------------------------")
        #Peticion de datos
        print("Carga los datos de una tarea")
        nom=input("Nombre de la tarea:  ")
        desc=input("Descripción de la tarea:    ")
        asig=input("Quien se va a encargar de la tarea: ")
        estado= input("En que estado se encuentra la tarea (pendiente / en progreso / completada):  ")
        # SE CHEQUEA SI EL DIA,MES Y ANIO SON 0 O NEGATIVO
        dia=int(input("Dia de vencimiento (valor numérico):"))
        while (dia<=0 or dia>=32):
            print("El valor ingresado no es valido")
            dia=int(input("Dia de vencimiento (valor numérico):"))
        mes=int(input("Mes de vencimiento (valor numérico):"))
        while (mes<=0 or mes>=13):
            print("El valor ingresado no es valido")
            mes=int(input("Mes de vencimiento (valor numérico):"))
        anio=int(input("año de vencimiento (valor numérico):"))
        while anio<=0:
            print("El valor ingresado no es valido")
            anio=int(input("Año de vencimiento (valor numérico):"))
        #Se asignan los datos a la tarea y se la agrega a la lista
        cargarTarea(t,nom,desc,asig,estado,dia,mes,anio)
        if estado=='en progreso':
            encolar(cola,t)
        agregarTarea(lista,t)
        print("La tarea fue agregada")
        input("--------------->  Presione Enter  <---------------") #Espera 
        os.system('cls' if os.name == 'nt' else 'clear') #Limpia la pantalla

    elif (opc=='b'): #Modifica la tarea
        print("Modificar una tarea")
        print("Que desea modificar de la tarea:")
        print("a.   Nombre")
        print("b.   Descripcion")
        print("c.   A quien se le asigno")
        print("d.   Estado")
        print("f.   Fecha de vencimiento")

        opc=input("Ingrese una opción: ")
        opc=opc.lower() # .lower() para que no distinga entre minusculas y mayusculas
        os.system('cls' if os.name == 'nt' else 'clear') #Limpia la pantalla

        if opc=='a': #Modificar nombre de la tarea
            print("Listado de tareas:\n")
            print("----------------------------------------------------------------------------") 
            imprimirTareas(lista)
            print("----------------------------------------------------------------------------") 
            print("\n\n") 
            
            #Busca la tarea por nombre
            nom=input("Ingrese el nombre de la tarea que quiera modificar:")
            encontrado=0
            for i in range(1,(tamanio(lista)+1)):
                aux=recuperarTarea(lista,i)
                if verNom(aux) == nom:
                    t=crearTarea()
                    t=recuperarTarea(lista,i)
                    print("La tarea fue encontrada con exito")
                    encontrado=1
                    break

            # verificar si encontró la tarea
            if encontrado != 0:
                if verEstado(t)=="en progreso":
                    #buscar tarea en cola y eliminarla
                    eliminarTarea_Cola(cola,t)
                eliminarTarea(lista,t)
                #print("La tarea '{}' ha sido eliminada.".format(nom))
                nom=input("Ingrese el nombre a modificar:")
                modNom(t,nom)
                agregarTarea(lista,t)
                if verEstado(t)=="en progreso":
                    #encolar la tarea modificada
                    encolar(cola,t)
            else:
                print("La tarea '{}' no existe en la lista.".format(nom))
                
        elif opc=='b': #Modificar descripcion de la tarea
            print("Listado de tareas:\n")
            print("----------------------------------------------------------------------------") 
            imprimirTareas(lista)
            print("----------------------------------------------------------------------------") 
            print("\n\n") 
            
            #Busca la tarea por nombre
            nom=input("Ingrese el nombre de la tarea que quiera modificar:")
            encontrado=0
            for i in range(0,(tamanio(lista)+1)):
                aux=recuperarTarea(lista,i)
                if verNom(aux) == nom:
                    t=crearTarea()
                    t=recuperarTarea(lista,i)
                    print("La tarea fue encontrada con exito")
                    encontrado=1
                    break
            
            # verificar si encontró la tarea
            if encontrado != 0:
                if verEstado(t)=="en progreso":
                    #buscar tarea en cola y eliminarla
                    eliminarTarea_Cola(cola,t)
                eliminarTarea(lista,t)
                #print("La tarea '{}' ha sido eliminada.".format(nom))
                desc=input("Ingrese la nueva descripcion:")
                modDesc(t,desc)
                agregarTarea(lista,t)
                if verEstado(t)=="en progreso":
                    #encolar la tarea modificada
                    encolar(cola,t)
            else:
                print("La tarea '{}' no existe en la lista.".format(nom))

            
        elif opc=='c': #Modificar a quien se le asigno la tarea
            print("Listado de tareas:\n")
            print("----------------------------------------------------------------------------") 
            imprimirTareas(lista)
            print("----------------------------------------------------------------------------") 
            print("\n\n") 
            
            #Busca la tarea por nombre
            nom=input("Ingrese el nombre de la tarea que quiera modificar:")
            encontrado=0
            for i in range(0,(tamanio(lista)+1)):
                aux=recuperarTarea(lista,i)
                if verNom(aux) == nom:
                    t=crearTarea()
                    t=recuperarTarea(lista,i)
                    print("La tarea fue encontrada con exito")
                    encontrado=1
                    break
            # verificar si encontró la tarea
            if encontrado != 0:
                if verEstado(t)=="en progreso":
                    #buscar tarea en cola y eliminarla
                    eliminarTarea_Cola(cola,t)
                eliminarTarea(lista,t)
                #print("La tarea '{}' ha sido eliminada.".format(nom))
                asig=input("Ingrese a quien se le asigno para modificar:")
                modAsig(t,asig)
                agregarTarea(lista,t)
                if verEstado(t)=="en progreso":
                    #encolar la tarea modificada
                    encolar(cola,t)
            else:
                print("La tarea '{}' no existe en la lista.".format(nom))

        elif opc=='d': #Modificar el estado de la tarea
            print("Listado de tareas:\n")
            print("----------------------------------------------------------------------------") 
            imprimirTareas(lista)
            print("----------------------------------------------------------------------------") 
            print("\n\n") 
            
            #Busca la tarea por nombre
            nom=input("Ingrese el nombre de la tarea que quiera modificar:")
            encontrado=0
            for i in range(0,(tamanio(lista)+1)):
                aux=recuperarTarea(lista,i)
                if verNom(aux) == nom:
                    t=crearTarea()
                    t=recuperarTarea(lista,i)
                    print("La tarea fue encontrada con exito")
                    encontrado=1
                    break
            
            # verificar si encontró la tarea
            if encontrado != 0:
                if verEstado(t)=="en progreso":
                    #buscar tarea en cola y eliminarla
                    eliminarTarea_Cola(cola,t)
                eliminarTarea(lista,t)
                #print("La tarea '{}' ha sido eliminada.".format(nom))
                estado=input("Ingrese el estado a modificar:")
                modEstado(t,estado)
                agregarTarea(lista,t)
                if verEstado(t)=="en progreso":
                    #encolar la tarea modificada
                    encolar(cola,t)
            else:
                print("La tarea '{}' no existe en la lista.".format(nom))

        elif opc=='f': #Modificar fecha de vencimiento de la tarea
            print("Listado de tareas:\n")
            print("----------------------------------------------------------------------------") 
            imprimirTareas(lista)
            print("----------------------------------------------------------------------------") 
            print("\n\n") 
            
            #Busca la tarea por nombre
            nom=input("Ingrese el nombre de la tarea que quiera modificar:")
            encontrado=0
            for i in range(1,(tamanio(lista)+1)):
                aux=recuperarTarea(lista,i)
                if verNom(aux) == nom:
                    t=crearTarea()
                    t=recuperarTarea(lista,i)
                    print("La tarea fue encontrada con exito")
                    encontrado=1
                    break
            
            # verificar si encontró la tarea
            if encontrado != 0:
                if verEstado(t)=="en progreso":
                    #buscar tarea en cola y eliminarla
                    eliminarTarea_Cola(cola,t)
                eliminarTarea(lista,t)
                #print("La tarea '{}' ha sido eliminada.".format(nom))

                dia=int(input("Dia de vencimiento (valor numérico):"))
                while (dia<=0 or dia>=32):
                    print("El valor ingresado no es valido")
                    dia=int(input("Dia de vencimiento (valor numérico):"))

                mes=int(input("Mes de vencimiento (valor numérico):"))
                while (mes<=0 or mes>=13):
                    print("El valor ingresado no es valido")
                    mes=int(input("Mes de vencimiento (valor numérico):"))

                anio=int(input("año de vencimiento (valor numérico):"))
                while anio<=0:
                    print("El valor ingresado no es valido")
                    anio=int(input("Año de vencimiento (valor numérico):"))

                modFecha(t,dia,mes,anio)
                agregarTarea(lista,t)
                if verEstado(t)=="en progreso":
                    #encolar la tarea modificada
                    encolar(cola,t)
            else:
                print("La tarea '{}' no existe en la lista.".format(nom))

            
        input("--------------->  Presione Enter  <---------------") #Espera 
        os.system('cls' if os.name == 'nt' else 'clear') #Limpia la pantalla

    elif (opc=='c'): #Eliminar una tarea
        print("Eliminar una tarea:)\n-----------------------------------------")
        print("Listado de tareas:\n") #lista las tareas para verlas
        print("----------------------------------------------------------------------------") 
        imprimirTareas(lista)
        print("\n\n") 
        #Busca la tarea por nombre
        nom=input("Ingrese el nombre de la tarea que quiera eliminar:")
        encontrado=0
        for i in range(1,(tamanio(lista)+1)):
            aux=recuperarTarea(lista,i)
            if verNom(aux) == nom:
                t=crearTarea()
                t=recuperarTarea(lista,i)
                print("La tarea fue encontrada con exito")
                encontrado=1
                break

        # Si se encontró la tarea, eliminarla
        if encontrado != 0:
            if verEstado(t)=="en progreso":
                #buscar tarea en cola y eliminarla
                eliminarTarea_Cola(cola,t)
            eliminarTarea(lista,t)
            print("La tarea '{}' ha sido eliminada.".format(nom))
        else:
            print("La tarea '{}' no existe en la lista.".format(nom))

        input("--------------->  Presione Enter  <---------------") #Espera
        os.system('cls' if os.name == 'nt' else 'clear') #Limpia la pantalla

    elif (opc=='d'): #Listar tareas
        #Listar tareas
        print("Listado de tareas:\n") #lista las tareas para verlas
        print("------------------------------------------------------------------------------------------") 
        if tamanio(lista)==0: #Me aseguro si esta vacio
            print("No hay tareas registradas.")
        else:
            imprimirTareas(lista)
        input("----------------->  Presionar Enter  <-----------------") #Espera
        os.system('cls' if os.name == 'nt' else 'clear') #Limpia la pantalla

    elif (opc=='e'): #Modificar fecha de vencimiento de tareas
        print("Modificar fecha de vencimiento de tareas:\n-----------------------------------------")
        print("Entre que fechas quiere modificar la fecha de vencimiento\n-----------------------------------------")

        print("Ingrese la primer fecha: ")
        dia=int(input("Ingrese el dia:  "))
        mes=int(input("Ingrese el mes:  "))
        anio=int(input("Ingrese el año:  "))
        fecha1= d.datetime(anio,mes,dia)

        print("Ingrese la segunda fecha: ")
        dia=int(input("Ingrese el dia:  "))
        mes=int(input("Ingrese el mes:  "))
        anio=int(input("Ingrese el año:  "))
        fecha2= d.datetime(anio,mes,dia)

        for i in range(1,(tamanio(lista)+1)):
            tarea=recuperarTarea(lista,i)
            if (fecha1.date() <= verFecha(tarea) <= fecha2.date()):
                print("-----------------------------------------------------------")
                print("La tarea que va a ser modificada es: ", verNom(tarea))
                print("Fecha anterior: ", verFecha(tarea))
                print("Cual va a ser la nueva fecha de vencimiento:")
                dia=int(input("Dia de vencimiento (valor numérico):"))
                while (dia<=0 or dia>=32):
                    print("El valor ingresado no es valido")
                    dia=int(input("Dia de vencimiento (valor numérico):"))
                mes=int(input("Mes de vencimiento (valor numérico):"))
                while (mes<=0 or mes>=13):
                    print("El valor ingresado no es valido")
                    mes=int(input("Mes de vencimiento (valor numérico):"))
                anio=int(input("año de vencimiento (valor numérico):"))
                while anio<=0:
                    print("El valor ingresado no es valido")
                    anio=int(input("Año de vencimiento (valor numérico):"))
                modFecha(tarea,dia,mes,anio)
                print("La nueva fecha es: ",verFecha(tarea))
            else:
                print("No se encontro ninguna tarea entre esas fechas")

        input("--------------->  Presione Enter  <---------------") #Espera
        os.system('cls' if os.name == 'nt' else 'clear') #Limpia la pantalla

    elif (opc=='f'): #Reporte de tareas
        print("Reporte de las tareas")
        print("-------------------------------------------------------") 
        if tamanio(lista)==0:
            print("No hay tareas registradas.")
        else:
            print(f"{RED}Tareas pendientes:{RESET}")
            print(f'{RED}{"Nombre" : <15}{"Descripcion" : <25}{"Asignado" : <15}{"Estado" : <15}{"Fecha de vencimiento"}{RESET}')
            for i in range(1,(tamanio(lista)+1)):
                tarea=recuperarTarea(lista,i)
                if verEstado(tarea)=="pendiente": #Chequeo el estado de la tarea
                    
                    print(f"{verNom(tarea) : <15}{verDesc(tarea) : <25}{verAsig(tarea) : <15}{verEstado(tarea) : <15}{verFecha(tarea)}")

            print(f"{YELLOW}Tareas en progreso:{RESET}")
            print(f'{YELLOW}{"Nombre" : <15}{"Descripcion" : <25}{"Asignado" : <15}{"Estado" : <15}{"Fecha de vencimiento"}{RESET}')
            for i in range(1,(tamanio(lista)+1)):
                tarea=recuperarTarea(lista,i)
                if verEstado(tarea)=="en progreso":
                    
                    print(f"{verNom(tarea) : <15}{verDesc(tarea) : <25}{verAsig(tarea) : <15}{verEstado(tarea) : <15}{verFecha(tarea)}")

            print(f"{GREEN}Tareas completadas:{RESET}")
            print(f'{GREEN}{"Nombre" : <15}{"Descripcion" : <25}{"Asignado" : <15}{"Estado" : <15}{"Fecha de Vencimiento"}{RESET}')
            for i in range(1,(tamanio(lista)+1)):
                tarea=recuperarTarea(lista,i)
                if verEstado(tarea)=="completada":
                    
                    print(f"{verNom(tarea) : <15}{verDesc(tarea) : <25}{verAsig(tarea) : <15}{verEstado(tarea) : <15}{verFecha(tarea)}")

        input("----------------->  Presionar Enter  <-----------------") #Espera
        os.system('cls' if os.name == 'nt' else 'clear') #Limpia la pantalla

    elif (opc=='g'): #Eliminar todas las tareas de un empleado ---tareas
        print("Eliminar todas las tareas de un empleado")
        empleado=input("Ingrese el nombre del empleado: ")
        empleado_encontrado=None
        i=1
        while (i)!=(tamanio(lista)):
            tarea=recuperarTarea(lista,i)
            if verAsig(tarea) == empleado:
                eliminarTarea(lista, tarea)
                empleado_encontrado=True
                i-=1
                if verEstado(tarea)=="en progreso":
                    eliminarTarea_Cola(cola,tarea)
            i+=1

        if empleado_encontrado is not None: ##verifica si no se encontro el empleado
            print("Las tareas de '{}' han sido eliminadas.".format(empleado))
        else:
            print("El empleado '{}' no existe en la lista.".format(empleado))

        input("--------------->  Presione Enter  <---------------") #Espera
        os.system('cls' if os.name == 'nt' else 'clear') #Limpia la pantalla

    elif (opc=='h'): #Listar las tareas en progreso
        #Lista las tareas en progreso
        imprimirCola(cola)
        
        input("--------------->  Presione Enter  <---------------")  # Espera
        os.system('cls' if os.name == 'nt' else 'clear')
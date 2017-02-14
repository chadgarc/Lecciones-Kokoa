
############### Habilitar comandos del sistema ##############

import os

############# Importacion de la clase Estudiante ############

from biblioteca.estudiantes import Estudiante

########################## Objetos ##########################

#Estudiante 1
e1 = Estudiante("","","","","")
e1.set_matricula("201616342")
e1.set_ci("0923416234")
e1.set_nombre("Christian Adrian Garcia Valenzuela")
e1.set_carrera("Ingenieria en Ciencias Computacionales")
e1.set_facultad("FIEC")

#Estudiante 2
e2 = Estudiante("","","","","")
e2.set_matricula("201645362")
e2.set_ci("1756423795")
e2.set_nombre("Julio Alberto Macias Espinoza")
e2.set_carrera("Ingenieria en Potencia")
e2.set_facultad("FIEC")

####################### Funciones #######################

def prints1():
    os.system ("clear")
    print ("\n\n\n\t\t\t\t\t\t\tLISTA DE ESTUDIANTES\n")
    print ("\t\t\t\t\t\t\t\t\t\t\t\tCupo disponible 1\n")
    print (e1)
    print (e2)
    print ("\n\t\t\t\t\t\t\t  AGREGAR ESTUDIANTE")
    print ("\n")

def prints2():
    os.system ("clear")
    print ("\n\n\n\t\t\t\t\t\t\tLISTA DE ESTUDIANTES\n")
    print ("\t\t\t\t\t\t\t\t\t\t\t\tCupo disponible 0\n")
    print (e1)
    print (e2)
    print (e3)
    print ("\n")

def reinicio():
    os.system ("python ./experimento.py")

def cambioatrib():
    os.system ("clear")
    print ("\n\t\t\t1. MATRICULA"+
            "\n\t\t\t2. C.I"+
            "\n\t\t\t3. NOMBRE"+
            "\n\t\t\t4. CARRERA"+
            "\n\t\t\t5. FACULTAD"+
            "\n\t\t\t6. TODOS"+
            "\n\t\t\t7. ATRAS")

def datosestudiantes():
    print ("\n\t\t\t1. PRIMER ESTUDIANTE"+
            "\n\t\t\t2. SEGUNDO ESTUDIANTE"+
            "\n\t\t\t3. TERCER ESTUDIANTE"+
            "\n\t\t\t4. ATRAS")

#########################################################
################## Corriendo el modulo ##################
#########################################################

#Mostrar datos de los dos primeros estudiantes

prints1()

#Ingresar datos de estudiante 3

e3 = Estudiante("","","","","")
e3.set_matricula(input ("\t\t\tINGRESE MATRICULA:\t\t\t"))
e3.set_ci(input ("\t\t\tINGRESE C.I:\t\t\t\t"))
e3.set_nombre(input ("\t\t\tINGRESE NOMBRE:\t\t\t\t"))
e3.set_carrera(input ("\t\t\tINGRESE CARRERA:\t\t\t"))
e3.set_facultad(input ("\t\t\tINGRESE FACULTAD:\t\t\t"))

#Realizar cambios y/o salir

a=0
while(1):
    #Mostrar datos de los tres estudiantes
    prints2()
    print ("\n\t\t\t 1. GUARDAR Y SALIR"
            +"\n\t\t\t 2. CAMBIAR DATOS")
    a=int(input("\n\t\t\t RESPUESTA:\t\t\t\t"))
    if(a==1):
        exit()
    if(a==2):
        datosestudiantes()
        b=int(input("\n\t\t\t DATOS A CAMBIAR:\t\t\t\t"))
        if(b==1):
            cambioatrib()
            c=int(input("\n\t\t\t RESPUESTA:\t\t\t\t"))
            if(c==1):
                e1.set_matricula(input ("\t\t\tINGRESE MATRICULA:\t\t\t"))
                prints2()
                continue
            if(c==2):
                e1.set_ci(input ("\t\t\tINGRESE C.I:\t\t\t\t"))
                prints2()
                continue
            if(c==3):
                e1.set_nombre(input ("\t\t\tINGRESE NOMBRE:\t\t\t\t"))
                prints2()
                continue
            if(c==4):
                e1.set_carrera(input ("\t\t\tINGRESE CARRERA:\t\t\t"))
                prints2()
                continue
            if(c==5):
                e1.set_facultad(input ("\t\t\tINGRESE FACULTAD:\t\t\t"))
                prints2()
                continue
            if(c==6):
                reinicio()
            if(c==7):
                prints2()
                continue
        if(b==2):
            cambioatrib()
            c=int(input("\n\t\t\t RESPUESTA:\t\t\t\t"))
            if(c==1):
                e2.set_matricula(input ("\t\t\tINGRESE MATRICULA:\t\t\t"))
                prints2()
                continue
            elif(c==2):
                e2.set_ci(input ("\t\t\tINGRESE C.I:\t\t\t\t"))
                prints2()
                continue
            elif(c==3):
                e2.set_nombre(input ("\t\t\tINGRESE NOMBRE:\t\t\t\t"))
                prints2()
                continue
            elif(c==4):
                e2.set_carrera(input ("\t\t\tINGRESE CARRERA:\t\t\t"))
                prints2()
                continue
            elif(c==5):
                e2.set_facultad(input ("\t\t\tINGRESE FACULTAD:\t\t\t"))
                prints2()
                continue
            elif(c==6):
                reinicio()
            elif(c==7):
                prints2()
                continue
        if(b==3):
            cambioatrib()
            c=int(input("\n\t\t\t RESPUESTA:\t\t\t\t"))
            if(c==1):
                e3.set_matricula(input ("\t\t\tINGRESE MATRICULA:\t\t\t"))
                prints2()
                continue
            if(c==2):
                e3.set_ci(input ("\t\t\tINGRESE C.I:\t\t\t\t"))
                prints2()
                continue
            if(c==3):
                e3.set_nombre(input ("\t\t\tINGRESE NOMBRE:\t\t\t\t"))
                prints2()
                continue
            if(c==4):
                e3.set_carrera(input ("\t\t\tINGRESE CARRERA:\t\t\t"))
                prints2()
                continue
            if(c==5):
                e3.set_facultad(input ("\t\t\tINGRESE FACULTAD:\t\t\t"))
                prints2()
                continue
            if(c==6):
                reinicio()
            if(c==7):
                prints2()
                continue
        if(b==4):
            prints2()
            continue
    if(a==exit()):
        exit()


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

#Estudiante nuevo
es = Estudiante("","","","","")
es.set_matricula("          ")
es.set_ci("             ")
es.set_nombre("")
es.set_carrera("")
es.set_facultad("")

####################### Funciones #######################

def prints1():
    os.system ("clear")
    print ("\n\n\n\t\t\t\t\t\t\tLISTA DE ESTUDIANTES\n")
    print ("\t\t\t\t\t\t\t\t\t\t\t\tCupo disponible 1\n")
    print (e1)
    print (e2)
    print ("\n\t\t\t\t\t\t\t  AGREGAR ESTUDIANTE")
#    print (es)
    print ("\n")

def prints2():
    os.system ("clear")
    print ("\n\n\n\t\t\t\t\t\t\tLISTA DE ESTUDIANTES\n")
    print ("\t\t\t\t\t\t\t\t\t\t\t\tCupo disponible 0\n")
    print (e1)
    print (e2)
    print (e3)
    print ("\n")

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

prints2()

#ENTRADA
import os
os.system("cls")
lista_grado=[]
lista_colegio=[]
lista_dni=[]
lista_cursos=[]
#PROCESO

print("------------Bienvenido al Aula Virtual------------")


nivel = input("Ingrese su nivel educativo<Primaria o Secuandaria>: ").lower()
while nivel !="primaria" and nivel != "secundaria": 
    nivel = input("Ingresa el nivel educativo correcto: ")

if nivel =="secundaria" :       
    grado= int(input("Ingresa el grado que estas cursando: "))
    while grado > 5:
        grado = int(input("Ingresa el grado correcto: "))

if nivel =="primaria" :
    grado= int(input("Ingresa el grado que estas cursando: "))

    while grado > 6:
        grado = int(input("Ingresa el grado correcto: "))         
            

edad = int(input("Ingresa tu edad: "))
while True:
    if edad > 18:
        print("Error, ingrese dato correcto")
        edad = input("Ingresa tu edad: ")
    else:
        break

colegio = input("Ingresa el nombre de tu colegio: ")
lista_colegio.append(colegio)
while True:
    if colegio == "":
        print("Error, ingrese dato correcto")
        colegio = input("Ingresa el nombre de tu colegio: ")
    else:
        break

nombre = input("Escriba su nombre: ")
while True:
    if nombre == "":
        print("Error, ingrese dato correcto")
        nombre = input("Escriba su nombre: ")
    else:
        break

apellido = input("Escriba su apellido: ")
while True:
    if apellido == "":
        print("Error, ingrese dato correcto")
        apellido = input("Escriba su apellido: ")
    else:
        break

dni =  int(input("Escriba el numero de su DNI: "))
lista_dni.append(dni)
while True:
    if dni <= 0:
        print("Error, ingrese dato correcto")
        dni =  int(input("Escriba el numero de su DNI: "))
    else:
        break


while True:
    cursos = input("Escriba el nombre del curso que va a llevar:")
    lista_cursos.append(cursos)     
    r = input("¿Desea añadir algun curso? <si o no>: ").lower()
    if r != "si":
        break

#SALIDA

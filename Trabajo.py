#Process
import os
os.system("cls")

print("------------Bienvenido al Aula Virtual------------")
grado = int(input("Ingresa el grado que estas cursando: "))
while True:
    if grado <= 0:
        print("Error, ingrese dato correcto")
        grado = int(input("Ingresa el grado que estas cursando: "))
    else:
        break

edad = int(input("Ingresa tu edad: "))
while True:
    if edad <= 0:
        print("Error, ingrese dato correcto")
        edad = input("Ingresa tu edad: ")
    else:
        break

colegio = input("Ingresa el nombre de tu colegio: ")
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
while True:
    if dni <= 0:
        print("Error, ingrese dato correcto")
        dni =  int(input("Escriba el numero de su DNI: "))
    else:
        break

cursos = input("Escriba los cursos que va a llevar:")
while True:
    if cursos == "":
        print("Error, ingrese dato correcto")
        cursos = input("Escriba los cursos que va a llevar:")
    else:
        break

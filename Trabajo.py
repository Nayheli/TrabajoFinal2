#ENTRADA
import os
os.system("cls")
lista_grado=[]
lista_colegio=[]
lista_dni=[]
lista_cursos=[]
#PROCESO

print("------------Bienvenido al Aula Virtual------------")
grado = int(input("Ingresa el grado que estas cursando: "))
lista_grado.append(grado)
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
        colegio = input("Ingresa el nombre de tu colegio: ")
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

cursos = input("Escriba los cursos que va a llevar:")
lista_cursos.append(cursos)
while True:
    if cursos == "":
        print("Error, ingrese dato correcto")
        cursos = input("Escriba los cursos que va a llevar:")
    else:
        break

#SALIDA
print(lista_grado)
print(lista_colegio)
print(lista_dni)
print(lista_cursos)
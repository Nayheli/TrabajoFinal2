#ENTRADA
import os
os.system("cls")
lista_grado=[]
lista_colegio=[]
lista_dni=[]
lista_cursos=[]
Horario_Cursos=[]
i = 0
#PROCESO

print("------------Bienvenido al Aula Virtual------------")


nivel = input("Ingrese su nivel educativo<Primaria o Secuandaria>: ").lower()
while nivel !="primaria" and nivel != "secundaria":
    print("-------Error-------") 
    nivel = input("Ingresa el nivel educativo correcto: ")

if nivel =="secundaria" :       
    grado= int(input("Ingresa el grado que estas cursando: "))
    while grado > 5:
        print("-----Error-----")
        grado = int(input("Ingresa el grado correcto: "))

if nivel =="primaria" :
    grado= int(input("Ingresa el grado que estas cursando: "))

    while grado > 6:
        print("-----Error-----")
        grado = int(input("Ingresa el grado correcto: "))         
            

edad = int(input("Ingresa tu edad: "))
while True:
    if edad > 18:
        print("-------Error------")
        print("Ingrese dato correcto")
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


if nivel =="secundaria":
    for i in range (0, 10):
        cursos = input("Escriba el nombre del curso que va a llevar:")
        lista_cursos.append(cursos)
        i += 1
if nivel =="primaria":
    for i in range (0,6):
        cursos = input("Escriba el nombre del curso que va a llevar:")
        lista_cursos.append(cursos) 
        i += 1                

#SALIDA
print("---------Datos del Alumno-----------")
print("Alumno:", nombre)
print("Edad:", edad)
print("Grado y nivel:", grado, nivel)
print("Registrado con el dni:", dni)
print("Cursos escogidos:", lista_cursos)


print("-------------Horarios--------------")
#horario de primaria
Horario1 = "7:00 am"
Horario2 = "9:00 am"
Horario3 = "11:00 am"
Recreo1 = "12:00 am - 12:30 pm"
Horario5 = "1:00 pm"
Horario6 = "2:00 pm"
#horario de secundaria
Horario7 = "7:00 am"
Horario8 = "9:00 am"
Horario9 = "11:00 am"
Recreo2 = "12:00 pm - 12:30 pm"
Horario11 = "1:00 pm"
Horario12 = "2:00 pm"
Horario13 = "3:00 pm" 



if nivel == "primaria":
    print(lista_cursos[2],"este curso lo llevaras a las",Horario1)





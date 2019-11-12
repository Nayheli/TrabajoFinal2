#ENTRADA
import os
os.system("cls")
lista_nombre=[]
lista_grado=[]
lista_colegio=[]
lista_dni=[]
lista_cursos=[]
Horario_Cursos=[]
lista_apellido=[]
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
        edad = int(input("Ingresa tu edad: "))
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
    print("-----Los cursos que tienes por elegir son:-----")
    print("Matemática, Lenguaje, Fisica, Química, Historia, Literatura, Raz.Matematica, Raz.Verbal, Computación, Ingles")
    for i in range (0,7):
        cursos = input("Escriba el nombre del curso que va a llevar:")
        lista_cursos.append(cursos)
        i += 1
if nivel =="primaria":
    print("Los cursos que tienes por elegir son:")
    print("Matemática, Comunicación, Ingles, Personal Social, Literatura, Raz.Matematica, Raz.Verbal, Computación, Ciencia, Educación fisica")
    for i in range (0,5):
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

#horario de clases
Horario0 = "7:00 am - 7:45 am"
Horario1 = "7:45 am - 8:30 am"
Horario2 = "8:30 am - 9:15 am"
Horario3 = "9:15 am - 10:00 am"
Recreo1 = "10:00 am - 10:15 am"
Horario4 = "10:15 am - 11:00 am"
Horario5 = "11:00 am - 11:45 am"
Recreo2 = "11:45 am - 12:00 pm"
Horario6 = "12:00 pm - 12:45 pm"
Horario7 = "12:45 pm - 1:30 pm"

print("-------------Horarios--------------")
if nivel == "primaria":
    print("-----Lunes-----")
    print(lista_cursos[0],"este curso lo llevaras a las",Horario1)
    print(lista_cursos[0],"este curso lo llevaras a las",Horario2)
    print(lista_cursos[1],"este curso lo llevaras a las",Horario3)
    print("El recreo empieza a las",Recreo1)
    print(lista_cursos[1],"este curso lo llevaras a las",Horario4)
    print(lista_cursos[2],"este curso lo llevaras a las",Horario5)
    print("El siguiente recreo empieza a las",Recreo2)
    print(lista_cursos[2],"este curso lo llevaras a las",Horario6)

    print("-----Martes-----")
    print(lista_cursos[3],"este curso lo llevaras a las",Horario1)
    print(lista_cursos[3],"este curso lo llevaras a las",Horario2)
    print(lista_cursos[4],"este curso lo llevaras a las",Horario3)
    print("El recreo empieza a las",Recreo1)
    print(lista_cursos[4],"este curso lo llevaras a las",Horario4)
    print(lista_cursos[1],"este curso lo llevaras a las",Horario5)
    print("El siguiente recreo empieza a las",Recreo2)
    print(lista_cursos[1],"este curso lo llevaras a las",Horario6)

    print("-----Miercoles-----")
    print(lista_cursos[2],"este curso lo llevaras a las",Horario1)
    print(lista_cursos[2],"este curso lo llevaras a las",Horario2)
    print(lista_cursos[4],"este curso lo llevaras a las",Horario3)
    print("El recreo empieza a las",Recreo1)
    print(lista_cursos[4],"este curso lo llevaras a las",Horario4)
    print(lista_cursos[3],"este curso lo llevaras a las",Horario5)
    print("El siguiente recreo empieza a las",Recreo2)
    print(lista_cursos[3],"este curso lo llevaras a las",Horario6)

    print("-----Jueves-----")
    print(lista_cursos[0],"este curso lo llevaras a las",Horario1)
    print(lista_cursos[0],"este curso lo llevaras a las",Horario2)
    print(lista_cursos[3],"este curso lo llevaras a las",Horario3)
    print("El recreo empieza a las",Recreo1)
    print(lista_cursos[3],"este curso lo llevaras a las",Horario4)
    print(lista_cursos[4],"este curso lo llevaras a las",Horario5)
    print("El siguiente recreo empieza a las",Recreo2)
    print(lista_cursos[4],"este curso lo llevaras a las",Horario6)

    print("-----Viernes-----")
    print(lista_cursos[2],"este curso lo llevaras a las",Horario1)
    print(lista_cursos[2],"este curso lo llevaras a las",Horario2)
    print(lista_cursos[3],"este curso lo llevaras a las",Horario3)
    print("El recreo empieza a las",Recreo1)
    print(lista_cursos[3],"este curso lo llevaras a las",Horario4)
    print(lista_cursos[4],"este curso lo llevaras a las",Horario5)
    print("El siguiente recreo empieza a las",Recreo2)
    print(lista_cursos[4],"este curso lo llevaras a las",Horario6)

if nivel == "secundaria":
    print("-----Lunes-----")
    print(lista_cursos[0],"este curso lo llevaras a las",Horario0)
    print(lista_cursos[0],"este curso lo llevaras a las",Horario1)
    print(lista_cursos[1],"este curso lo llevaras a las",Horario2)
    print(lista_cursos[1],"este curso lo llevaras a las",Horario3)
    print("El recreo empieza a las",Recreo1)
    print(lista_cursos[2],"este curso lo llevaras a las",Horario4)
    print(lista_cursos[2],"este curso lo llevaras a las",Horario5)
    print("El siguiente recreo empieza a las",Recreo2)
    print(lista_cursos[3],"este curso lo llevaras a las",Horario6)
    print(lista_cursos[3],"este curso lo llevaras a las",Horario7)

    print("-----Martes-----")
    print(lista_cursos[4],"este curso lo llevaras a las",Horario0)
    print(lista_cursos[4],"este curso lo llevaras a las",Horario1)
    print(lista_cursos[5],"este curso lo llevaras a las",Horario2)
    print(lista_cursos[5],"este curso lo llevaras a las",Horario3)
    print("El recreo empieza a las",Recreo1)
    print(lista_cursos[6],"este curso lo llevaras a las",Horario4)
    print(lista_cursos[6],"este curso lo llevaras a las",Horario5)
    print("El siguiente recreo empieza a las",Recreo2)
    print(lista_cursos[0],"este curso lo llevaras a las",Horario6)
    print(lista_cursos[0],"este curso lo llevaras a las",Horario7)

    print("-----Miercoles-----")
    print(lista_cursos[1],"este curso lo llevaras a las",Horario0)
    print(lista_cursos[1],"este curso lo llevaras a las",Horario1)
    print(lista_cursos[3],"este curso lo llevaras a las",Horario2)
    print(lista_cursos[3],"este curso lo llevaras a las",Horario3)
    print("El recreo empieza a las",Recreo1)
    print(lista_cursos[2],"este curso lo llevaras a las",Horario4)
    print(lista_cursos[2],"este curso lo llevaras a las",Horario5)
    print("El siguiente recreo empieza a las",Recreo2)
    print(lista_cursos[4],"este curso lo llevaras a las",Horario6)
    print(lista_cursos[4],"este curso lo llevaras a las",Horario7)

    print("-----Jueves-----")
    print(lista_cursos[5],"este curso lo llevaras a las",Horario0)
    print(lista_cursos[5],"este curso lo llevaras a las",Horario1)
    print(lista_cursos[6],"este curso lo llevaras a las",Horario2)
    print(lista_cursos[6],"este curso lo llevaras a las",Horario3)
    print("El recreo empieza a las",Recreo1)
    print(lista_cursos[1],"este curso lo llevaras a las",Horario4)
    print(lista_cursos[1],"este curso lo llevaras a las",Horario5)
    print("El siguiente recreo empieza a las",Recreo2)
    print(lista_cursos[0],"este curso lo llevaras a las",Horario6)
    print(lista_cursos[0],"este curso lo llevaras a las",Horario7)

    print("-----Viernes-----")
    print(lista_cursos[4],"este curso lo llevaras a las",Horario0)
    print(lista_cursos[4],"este curso lo llevaras a las",Horario1)
    print(lista_cursos[5],"este curso lo llevaras a las",Horario2)
    print(lista_cursos[5],"este curso lo llevaras a las",Horario3)
    print("El recreo empieza a las",Recreo1)
    print(lista_cursos[2],"este curso lo llevaras a las",Horario4)
    print(lista_cursos[2],"este curso lo llevaras a las",Horario5)
    print("El siguiente recreo empieza a las",Recreo2)
    print(lista_cursos[1],"este curso lo llevaras a las",Horario6)
    print(lista_cursos[1],"este curso lo llevaras a las",Horario7)



print("-----Material Didactico------")

print("||||||   ||||    ||||   ||||||            ")
print("    ||     |||  |||         ||    ||||||||")
print("||||         ||||       ||||              ")
print("||         |||  |||     ||        ||||||||")
print("||||||   ||||    ||||   ||||||            ")

a = int(input("Resolver el siguiente problema: "))

while True:
    if a == 4:
        print("Respuesta Correcta!")
        break
    else:
        print("Respuesta Incorrecta :( ")
        a = int(input("Resolver el siguiente problema: "))


for i in apellido:
    if i == 'a': 
        lista_apellido.append(i)
    elif i == 'e': 
        lista_apellido.append(i)
    elif i == 'i': 
        lista_apellido.append(i)
    elif i == 'o': 
        lista_apellido.append(i)
    elif i == 'u': 
        lista_apellido.append(i)

print("---------Simulación de su promedio hasta el momento-----------")
if lista_apellido[0]=="a":
    print("Su promedio de todos los cursos hasta el momento es : 15")
elif  lista_apellido[0]=="e" :
    print("Su promedio de todos los cursos hasta el momento es : 13")
elif lista_apellido[0]=="i":
    print("Su promedio de todos los cursos hasta el momento es : 14")
elif lista_apellido[0]=="o":
    print("Su promedio de todos los cursos hasta el momento es : 16")
elif lista_apellido[0]=="u":
    print("Su promedio de todos los cursos hasta el momento es : 18")   
     

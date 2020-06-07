'''
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email.
Además deberá mostrar un menú con las siguientes opciones

Añadir contacto
Lista de contactos
Buscar contacto
Editar contacto
Cerrar agenda
'''

import os
from time import sleep

def menu():
    os.system("clear")
    print("********* MENU **********")
    print("1. Anade contacto ")
    print("2. Lista de contactos ")
    print("3. Buscar contactos ")
    print("4. Editar contacto ")
    print("5. Cerrar agenda ")
    print("*************************")

miLista=[]

def anadirContacto(nombre):
    miLista.append(nombre)


def mostrarlista():
    for i in range(len(miLista)):
        print((i+1), end="")
        print("".join(miLista[i]))

def buscarContacto(nombre):
    if(nombre in miLista):
        print("Si existe")
    else:
        print("No existe")


def editarContacto(nombreQuitar, nombreNuevo):
    if nombreQuitar not in miLista:
        print("No existe")
    else:
        for i in range(len(miLista)):
            if(miLista[i]==nombreQuitar):
                miLista[i] = nombreNuevo
                print("nombre modificado!")
    mostrarlista()


menu()
start=True
while(start):
    try:
        elegir=int(input("Opcion>>"))

        if(elegir==1):
            #Añadir contacto
            anade = input("Dime nombre a agregar:")
            anadirContacto(anade)
            print("%s anadido con exito."%(anade))
            print("Lista actualizada.")
        elif(elegir==2):
            if(len(miLista)<=0):
                print("Lista esta vacia")
            else:
                print("Lista actualizada:")
                mostrarlista()
        elif(elegir==3):
            nombre=input("Nombre a buscar:")
            buscarContacto(nombre)
        elif(elegir==4):
            nombrequitar=input("Nombre que deseas modificar:")
            nombreNuevo=input("Nombre nuevo:")
            editarContacto(nombrequitar, nombreNuevo)
        elif(elegir==5):
            print("Adios")
            start=False
        else:
            print("Opcion incorrecta")
            sleep(2)
    except IOError as e:
        print(e)
        start=False
    except:
        print("Error")
        start=False
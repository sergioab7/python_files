'''
 Juego del Ahorcado
 (5 Vidas)
'''
from random import randint
import os


palabras=["tenerife", "salchicha", "dinamarca", "peluche"]

def palabra_random():
    elegir_palabra_random=palabras[randint(0,len(palabras))-1]
    return elegir_palabra_random

def logica():
    palabra_ordenador=palabra_random()
    vidas=5
    pista=["*"]*len(palabra_ordenador)
    try:
        for i in range(0, vidas):
            print("--------- TURNO %s ---------"%(i+1))
            print()
            print("".join(pista))
            print()
            print("Palabra: %s"%(palabra_ordenador))
            letra=str(input("Dime letra>>"))
            while(letra not in 'abcdefghijklmnopqrstuvwxyz'):
                letra=input("Dime letra>>")

            if(letra in palabra_ordenador):
                print("Letra %s encontrada. "%(letra))
            else:
                print("Letra %s no encontrada."%(letra))
                i += 1
                print("Te quedan: %s vidas"%(5-i))

            for i,j in enumerate(palabra_ordenador):
                if(letra==j):
                    pista[i] = letra

            print("".join(pista))

            if (i > 0):
                palabra_resuelta = input("¿Sabes ya la palabra?>>")
                if (palabra_resuelta == palabra_ordenador):
                    print("¡Has ganado!")
                    break
            else:
                pass

            if(i==5):
                print("Game over")


    except Exception as e:
        print(e)

def menu():
    os.system("clear")
    print("##########¡Bienvenido al Ahorcado!##########")
    print("Palabras disponibles: ")
    for i in palabras:
        print("[%s] " % (i), end="")
    print("")
    print("############################################")


def juego():
    menu()

    logica()


juego()
'''
Juego de barcos
'''

from random import randint
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0

# 4 * 5
matriz=[]

for i in range(0,4):
    matriz.append(["0"]*4)

def mostrar_raiz(matriz):
    for i in matriz:
        print(" ".join(i))

#mostrar_raiz(matriz)

#Barco hundido
#matriz_raiz[row][column]
#matriz_raiz[fila_random][columna_random]

def fila_random(matriz):
    return randint(0,len(matriz)-1)

def columna_random(matriz):
    return randint(0, len(matriz[0])-1)

fila_barco_random = fila_random(matriz)   #Fila
columna_barco_random = columna_random(matriz)  #Columna

print("Solucion: fila:%s columna: %s"%(fila_barco_random,columna_barco_random))

print("------ JUEGO DE HUNDIR LA FLOTA --------")
for i in range(0,3):

   print("---- INTENTO NUMERO: %s ----"%(i+1))

   fila_barco_usuario = int(input("FILA>>"))
   columna_barco_usuario = int(input("COLUMNA>>"))

   if(fila_barco_random==fila_barco_usuario and columna_barco_random==columna_barco_usuario):
       print("¡Has acertado!")
       matriz[fila_barco_usuario][columna_barco_usuario] = "X"
       mostrar_raiz(matriz)
       break
   else:
       if(fila_barco_usuario not in range(4) or columna_barco_usuario not in range(4)):
             print("Fuera de rango")
             i -= 1
       elif(fila_barco_usuario != fila_barco_random or columna_barco_usuario != columna_barco_random):
             i -= 1
             print("Fallaste!")
             matriz[fila_barco_usuario][columna_barco_usuario] = "O"
             mostrar_raiz(matriz)

       if(i>2):
            print("Game over")
            break

'''
CARA O CRUZ
'''
from random import randint
opciones=["CARA", "CRUZ"]
print("### ¡JUEGO CARA O CRUZ! ###")
n_rondas=int(input("Dime numero de rondas>>"))
for i in range(0, n_rondas):
    moneda=opciones[randint(0,len(opciones))-1]
    opcion_ordenador=""
    print("RONDA: %s"%(i+1))
    pregunta_usuario=input("¿Cara o Cruz? >>")
    usuario = pregunta_usuario.upper()
    if(usuario=="cara"):
        opcion_ordenador="cruz"
    else:
        opcion_ordenador="cara"
    print("El ordenador elige: %s"%(opcion_ordenador))
    if(moneda==usuario):
        print("Ha salido: %s" % (moneda))
        print("Has ganado!")
    else:
        print("Ha salido: %s" % (moneda))
        print("El ordenador ha ganado!")







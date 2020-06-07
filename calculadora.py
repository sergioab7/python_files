from tkinter import *

'''CALCULADORA'''

raiz=Tk()
raiz.title("Calculadora")
raiz.geometry("250x220+500+200")
raiz.resizable(0,0)

#---------------- FRAME PRINCIPAL ----------------------------
miFrame=Frame(raiz)
miFrame.pack()

resultado=0
operacion=""

#----------------- PANTALLA ------------------------

numeroPantalla=StringVar() #Variable

pantalla = Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=0, column=1, padx=10, pady=25,columnspan=4)
pantalla.config(bg="black", fg="white", justify="right", relief="groove", bd=1)
pantalla.focus_set()

#---------------- FUNCIONES --------------------------

def borrar():
    global resultado
    resultado=0
    numeroPantalla.set("")


def numeroPulsado(num):
    global operacion

    if(operacion != ""):

        numeroPantalla.set(num)

        operacion=""

    else:
        numeroPantalla.set(numeroPantalla.get()+num)

#----------------- FUNCION SUMA --------------------
def sumar(num):
    global operacion
    global resultado

    operacion="sumar"

    resultado += int(num)

    numeroPantalla.set(resultado)

#---------------- FUNCION RESTA ---------------------
num1=0
contador_resta=0

def restar(num):

    global operacion
    global resultado
    global num1
    global contador_resta

    if(contador_resta==0):
        num1=int(num)
        resultado=num1
    else:
        if(contador_resta==1):
            resultado=num1-int(num)
        else:
            resultado=int(resultado)-int(num)

        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()

    contador_resta=contador_resta+1
    operacion="resta"
    borrar()



def el_resultado():
    global resultado
    global operacion
    global contador_resta

    if(operacion=="suma"):
        numeroPantalla.set(resultado + int(numeroPantalla.get()))
        resultado=0
    elif(operacion=="resta"):
        numeroPantalla.set(resultado - int(numeroPantalla.get()))
        resultado=0
        contador_resta=0



#---------------- BOTON 1 (7-8-9-/) -----------------

boton7=Button(miFrame, text="7", width=4, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1, padx=2, pady=2)
boton8=Button(miFrame, text="8", width=4,command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2,padx=2, pady=2)
boton9=Button(miFrame, text="9", width=4,command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3,padx=2, pady=2)
botonDiv=Button(miFrame, text="/", width=4)
botonDiv.grid(row=2,column=4,padx=2, pady=2)

#---------------- BOTON 2 (4-5-6-X) -----------------

boton4=Button(miFrame, text="4", width=4,command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1,padx=2, pady=2)
boton5=Button(miFrame, text="5", width=4,command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2,padx=2, pady=2)
boton6=Button(miFrame, text="6", width=4,command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3,padx=2, pady=2)
botonMult=Button(miFrame, text="x", width=4)
botonMult.grid(row=3,column=4,padx=2, pady=2)

#---------------- BOTON 3 (1-2-3- - ) -----------------

boton1=Button(miFrame, text="1", width=4,command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1,padx=2, pady=2)
boton2=Button(miFrame, text="2", width=4,command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2,padx=2, pady=2)
boton3=Button(miFrame, text="3", width=4,command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3,padx=2, pady=2)
botonRes=Button(miFrame, text="-", width=4,command=lambda:restar(numeroPantalla.get()))
botonRes.grid(row=4,column=4,padx=2, pady=2)

#---------------- BOTON 4 (signos y 0) -----------------

boton0=Button(miFrame, text="0", width=4,command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1,padx=2, pady=2)
botonComa=Button(miFrame, text=",", width=4,command=lambda:numeroPulsado("."))
botonComa.grid(row=5,column=2,padx=2, pady=2)
botonIgual=Button(miFrame, text="=", width=4, command=lambda:el_resultado())
botonIgual.grid(row=5, column=3,padx=2, pady=2)
botonSum=Button(miFrame, text="+", width=4, command=lambda:sumar(numeroPantalla.get()))
botonSum.grid(row=5,column=4,padx=2, pady=2)

botonBorrar=Button(miFrame, text="CE", width=22,command=lambda:borrar())
botonBorrar.grid(row=6,column=1,padx=2, pady=2,columnspan=4)







raiz.mainloop()
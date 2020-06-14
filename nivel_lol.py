#https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Wexeyen?api_key=RGAPI-d075160a-2b86-4e6a-86f0-1cc0dbd96fae

#Nivel
import requests
from tkinter import Tk
from tkinter import *


root=Tk()
root.geometry("600x400+400+200")
root.resizable(0,0)

def API(nombre):
    URL="https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/%s?api_key=RGAPI-d075160a-2b86-4e6a-86f0-1cc0dbd96fae"%nombre
    response=requests.get(URL)
    if(response.status_code==200):
        js=response.json()
        mostrarNivel['text']=js['summonerLevel']
    else:
        mostrarNivel['text']="None"







root.title("Nivel de Invocador")

informacion=Label(root)
informacion.pack()
informacion["text"]="Introduce el nombre del jugador y verás su nivel de invocador."

etiquetaNombre=Label(root, text="Nombre: ",font=("Courier",20,"normal"))
etiquetaNombre.place(x=60, y=60, width=100, height=30)

buscar_jugador=Entry(root,font=("Courier",20,"normal"),justify="center")
buscar_jugador.pack(padx=30,pady=30)

botonContinuar=Button(root, text="Aceptar", command=lambda:API(buscar_jugador.get()))
botonContinuar.place(x=260, y=100, width=100, height=30)

etiquetaNivel=Label(root,text="NIVEL:",font=("Courier",20,"normal"))
etiquetaNivel.place(x=90, y=200, width=100, height=30)

mostrarNivel=Label(root,font=("Courier",20,"normal"))
mostrarNivel.place(x=200, y=200, width=100, height=30)



root.mainloop()

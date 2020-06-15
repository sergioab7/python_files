from tkinter import *
from bs4 import BeautifulSoup
import requests
import pandas as pd
# -*- coding: UTF8 -*-

root=Tk()
root.title("Puntos Liga Futbol")
root.geometry("350x550+400+200")

def eleccion_Inglaterra():
    mostrarClasificacion['text'] = " "
    url = "https://resultados.as.com/resultados/futbol/inglaterra/clasificacion/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    # Equipos
    clasi = soup.find_all("span", class_="nombre-equipo")
    equipos = list()

    count_equipos = 0
    for i in clasi:
        if count_equipos < 20:
            equipos.append(i.text)
        else:
            break
        count_equipos += 1

    # Puntos
    pt = soup.find_all("td", class_="destacado")
    puntos = list()

    count = 0
    for i in pt:
        if (count < 20):
            puntos.append(i.text)
        else:
            break
        count += 1

    df = pd.DataFrame({"Nombre:": equipos, "Puntos:": puntos}, index=(list(range(1, 21))))
    mostrarClasificacion['text'] = df


def eleccion_Italia():
    mostrarClasificacion['text'] = " "
    url = "https://resultados.as.com/resultados/futbol/italia/clasificacion/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    # Equipos
    clasi = soup.find_all("span", class_="nombre-equipo")
    equipos = list()

    count_equipos = 0
    for i in clasi:
        if count_equipos < 20:
            equipos.append(i.text)
        else:
            break
        count_equipos += 1

    # Puntos
    pt = soup.find_all("td", class_="destacado")
    puntos = list()

    count = 0
    for i in pt:
        if (count < 20):
            puntos.append(i.text)
        else:
            break
        count += 1

    df = pd.DataFrame({"Nombre:": equipos, "Puntos:": puntos}, index=(list(range(1, 21))))
    mostrarClasificacion['text'] = df

def eleccion_España():
    mostrarClasificacion['text'] = " "
    url = "https://resultados.as.com/resultados/futbol/primera/clasificacion/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    # Equipos
    clasi = soup.find_all("span", class_="nombre-equipo")
    equipos = list()

    count_equipos = 0
    for i in clasi:
        if count_equipos < 20:
            equipos.append(i.text)
        else:
            break
        count_equipos += 1

    # Puntos
    pt = soup.find_all("td", class_="destacado")
    puntos = list()

    count = 0
    for i in pt:
        if (count < 20):
            puntos.append(i.text)
        else:
            break
        count += 1

    df=pd.DataFrame({"Nombre:":equipos, "Puntos:":puntos}, index=(list(range(1,21))))
    mostrarClasificacion['text']=df

def eleccion_Alemana():
    mostrarClasificacion['text'] = " "
    url = "https://resultados.as.com/resultados/futbol/alemania/clasificacion/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    # Equipos
    clasi = soup.find_all("span", class_="nombre-equipo")
    equipos = list()

    count_equipos = 0
    for i in clasi:
        if count_equipos < 18:
            equipos.append(i.text)
        else:
            break
        count_equipos += 1

    # Puntos
    pt = soup.find_all("td", class_="destacado")
    puntos = list()

    count = 0
    for i in pt:
        if (count < 18):
            puntos.append(i.text)
        else:
            break
        count += 1

    df = pd.DataFrame({"Nombre:": equipos, "Puntos:": puntos}, index=(list(range(1, 19))))
    mostrarClasificacion['text'] = df


def eleccion_Francia():
    mostrarClasificacion['text']=" "
    mostrarClasificacion['text'] = "1. PSG"

def liga(mi_liga):
    mostrarClasificacion['text'] = " "
    if(mi_liga=="España"):
        eleccion_España()
    elif(mi_liga=="Inglaterra"):
        eleccion_Inglaterra()
    elif(mi_liga=="Italia"):
        eleccion_Italia()
    elif (mi_liga=="Alemana"):
        eleccion_Alemana()
    elif(mi_liga=="Francia"):
        eleccion_Francia()
    else:
        mostrarClasificacion['text'] += "Liga: \n España/Inglaterra/Italia/Alemana/Francia"





mostrarLiga = Label(root, text="Liga: ", font=("Courier", 20, "normal"))
mostrarLiga.place(x=50, y=20, width=80, height=40)

miEntrada=Entry(root, justify="center")
miEntrada.place(x=130,y=20,width=120,height=40)

botonAceptar=Button(root, text="Aceptar", command=lambda:liga(miEntrada.get()))
botonAceptar.place(x=130, y=60, width=120, height=20)

mostrarClasificacion=Label(root,bg="black", fg="white")
mostrarClasificacion.place(x=0,y=80, width=350,height=550)


root.mainloop()

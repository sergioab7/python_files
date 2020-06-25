palabras=["Hello","Alaska","Dad","Peace"]


primera_fila=["q","w","e","r","t","y","u","i","o","p"]
segunda_fila=["a","s","d","f","g","h","j","k","l"]
tercera_fila=["z","x","c","v","b","n","m"]
       
    
primera=list(map(lambda x:x.upper(),primera_fila))
segunda=list(map(lambda x:x.upper(),segunda_fila))
tercera=list(map(lambda x:x.upper(),tercera_fila))

laspalabras=list(map(lambda x: x.upper(), palabras))

damelo=[]
letras_primera=""
letras_segunda=""
letras_tercera=""
for i in laspalabras:
    for j in i:
        for letra in segunda:
            if(letra==j):
                letras_segunda += letra
        for letra in primera:
            if(letra==j):
                letras_primera += letra
        for letra in tercera:
            if(letra==j):
                letras_tercera += letra

esta=[]
for i in laspalabras:
  if(i in letras_segunda or i in letras_primera or i in letras_tercera):
    esta.append(i)
  else:
    pass

print(esta)

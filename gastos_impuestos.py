'''
Introduce el año inicial:  2015
Introduce el año final:  2018
Ingresos del año 2015:  100000
Gastos del año 2015:  80000
Ingresos del año 2016:  120000
Gastos del año 2016:  125000
Ingresos del año 2017:  140000
Gastos del año 2017:  100000
Ingresos del año 2018:  150000
Gastos del año 2018:  125000
[20000.0, -5000.0, 40000.0, 25000.0]
[True, False, True, True]
Años con beneficios:  [2015, 2017, 2018]
Años con pérdidas:  [2016]
'''

gastos=[]
beneficios=[]

fecha_inicio=int(input("Registra la fecha de inicio>>"))
fecha_final=int(input("Registra la fecha final>>"))
anios=(fecha_final-fecha_inicio)+1

sumatoria=[]
anios_negativos=[]
anios_positivos=[]

for i in range(0,anios):
    ingresos=float(input("Ingresos del año %s>>"%(fecha_inicio+i)))
    gastos_anio=float(input("Gastos del año %s>>"%(fecha_inicio+i)))
    if(ingresos>gastos_anio):
        anios_positivos.append(fecha_inicio+i)
    else:
        anios_negativos.append(fecha_inicio+i)

    beneficios.append(ingresos)
    gastos.append(gastos_anio)

    fecha_inicio+i

for i in range(len(gastos)):
    resultado = beneficios[i] - gastos[i]
    sumatoria.append(resultado)


print("Beneficios",beneficios)
print("Gastos",gastos)
print("Sumatoria", sumatoria)
print()
print("Años con beneficios: %s"%(anios_positivos))
print("Años con perdidas: %s"%(anios_negativos))


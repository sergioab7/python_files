'''
Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura.
El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar.


Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario.
Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario.
Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

'''

factura=dict()


def menu():
	print('''
	---- PROGRAMA FACTURA 1.0 -------
		1. Añadir Factura
		2. Pagar Factura
		3. Terminar Programa
	''')

def cantidad_total():
	print("-----Lista-----")
	for i,j in factura.items():
		print(i,j)

def add_Factura(numero,coste):
	#factura[numero]=coste
	if(numero in factura):
		return "existe"
	else:
		factura[numero]=coste

def pagar_Factura(num):
	#del factura[num]
	if(num in factura):
		del factura[num]
	else:
		return "existe"

menu()

start=True
while(start):
	opcion=int(input("Selecciona la opcion que quieres:"))
	if(opcion==1):
		print("Opcion seleccionada: Añadir Factura...")
		numero_factura=int(input("Dime numero de factura:"))
		coste_factura=int(input("Coste de factura:"))
		resultado = add_Factura(numero_factura,coste_factura)
		if(resultado=="existe"):
			print("Ya existe")
			cantidad_total()
		else:
			cantidad_total()

	elif(opcion==2):
		print("Opcion seleccionada: Pagar factura")
		cantidad_total()
		numero=int(input("Que factura deseas pagar?"))
		pago=pagar_Factura(numero)
		if(pago=="existe"):
			print("No existe")
			cantidad_total()
		else:
			print("Factura pagada con exito")
			cantidad_total()

	elif(opcion==3):
		print("Programa terminado.")
		break
	else:
		print("Opcion incorrecta")
class Producto:
	def __init__(self, codigo, nombre, precio):
		self.__codigo = codigo
		self.__nombre = nombre
		self.__precio = precio

	@property
	def codigo(self):
		return self.__codigo

	@codigo.setter
	def codigo(self,valor):
		self.__codigo = valor

	@property
	def nombre(self):
		return self.nombre

	@nombre.setter
	def nombre(self, valor):
		self.__nombre = valor

	@property
	def precio(self):
		return self.precio

	@precio.setter
	def precio(self, valor):
		self.__precio = valor

	def calcular_total(self, unidad):
		return self.__precio * unidad

	def __str__(self):
		return "Codigo: {} Nombre: {} Precio: {}".format(str(self.__codigo), self.__nombre, str(self.__precio))

class Pedido:

	def __init__(self):
		self.__productos = []
		self.__cantidad = []

	def anadir_producto(self, producto, cantidad):

		if not isinstance(producto, Producto):
			raise Exception('anadir_producto: producto debe ser de la clase producto')

		if not isinstance(cantidad, int):
			raise Exception('anadir_producto: cantidad debe ser un numero')

		if cantidad <= 0:
			raise Exception("anadir_producto: cantidad debe ser mayor que 0")

		if producto in self.__productos:
			indice = self.__productos.index(producto)
			self.__cantidad[indice] = self.__cantidad[indice] + cantidad
		else:
			self.__productos.append(producto)
			self.__cantidad.append(cantidad)

	def eliminar_producto(self,producto):
		if not isinstance(producto, Producto):
			raise Exception('eliminar_producto: producto debe ser de la clase producto')

		if producto in self.__productos:
			indice = self.__productos.index(producto)
			del self.__productos[indice]
			del self.__cantidad[indice]
		else:
			raise Exception("eliminar producto: no existe el producto ")


	def total_pedido(self):
		total=0

		for (p,c) in zip(self.__productos, self.__cantidad):
			total = total + p.calcular_total(c)

		return total

	def mostrar_pedido(self):

		for (p,c) in zip(self.__productos,self.__cantidad):
			print("Producto -> " , p , "Cantidad:", str(c))



p1 = Producto(1, "Marte", 2)
p2 = Producto(2, "Jupiter", 3)
p3 = Producto(3, "Saturno", 6)


pedido = Pedido()

try:
	pedido.anadir_producto(p1,5)
	pedido.anadir_producto(p2, 5)
	pedido.anadir_producto(p3, 5)

	pedido.mostrar_pedido()

	pedido.eliminar_producto(p1)
	print("Total pedido:" + str(pedido.total_pedido()))

	pedido.mostrar_pedido()


except Exception as e:
	print(e)
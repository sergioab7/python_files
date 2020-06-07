from time import sleep

class Cuenta:

    def __init__(self, titular, cantidad):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, valor):
        self.__titular=valor

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, valor):
        self.__cantidad=valor

    def mostrar(self):
        return "Titular: {} Cantidad: {}".format(self.__titular, self.__cantidad)

    def ingresar(self, cantidad_ingresada):

        if not isinstance(cantidad_ingresada, float):
            raise("Cantidad erronea, debe ser un numero")

        if(cantidad_ingresada<0):
            print("Error. La cantidad no debe ser negativa.")
            print("Cantidad de dinero: {}".format(self.__cantidad))

        if(cantidad_ingresada>0):
            dinero_Total=cantidad_ingresada + self.__cantidad
            print("Dinero ingresado con existo. Total en la cuenta: {}".format(dinero_Total))
            self.__cantidad=dinero_Total

    def retirar(self, dinero_retirar):
        if not isinstance(dinero_retirar, float):
            raise("Debe ser numero")

        if(dinero_retirar>self.__cantidad):
            print("Error. En la cuenta tienes menos dinero: {}".format(self.__cantidad))
        if(dinero_retirar<0):
            print("Error. No puedes retirar numeros negativos.")

        if(dinero_retirar<self.__cantidad):
            retiro_dinero=self.__cantidad-dinero_retirar
            print("Dinero retirado con existo. Te quedan: {} euros.".format(retiro_dinero))
            self.__cantidad=retiro_dinero


c = Cuenta("Sergio", 500.0)
print(c.mostrar())
sleep(1)
c.ingresar(300.0)
sleep(1)
c.retirar(200.0)
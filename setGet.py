class Ejemplo:
    def __init__(self):
        self.__atributo_privado = 30

    def getter(self):
        return self.__atributo_privado
    
    def setter(self, valor):
        if valor > 0:
            self.__atributo_privado = valor
        else:
            print("El valor debe ser positivo")


ejemplo = Ejemplo()
print(ejemplo.getter())
ejemplo.setter(2) #Se puede modificar un atributo privado de esta manera
print(ejemplo.getter())
ejemplo.__atributo_privado = 50 #No se puede modificar un atributo privado de esta manera
print(ejemplo.getter())


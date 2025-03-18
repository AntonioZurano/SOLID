# Ejercicio herencia Simple

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonidos(self):
        pass

class Conejo (Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonidos(self):
        return "Hace sonidos de conejo"
    

mi_conejo = Conejo("Bugs Bunny")
#print(mi_conejo.nombre)
#print(mi_conejo.hacer_sonidos())

# Ejemplo 2 Herencia multiple

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def conducir(self):
        return "Rum rum"

#class Persona(Vehiculo, Animal):
#    def __init__(self, nombre, marca, modelo):
#        Vehiculo.__init__(self, marca, modelo)
#        Animal.__init__(self, nombre)
#    def presentarse(self):
#        return f"Me llamo {self.nombre} y conduzco un {self.marca} {self.modelo}"
#    def hacer_sonidos(self):
#        return "Hace sonidos de persona"

#persona1 = Persona("Juan", "Toyota", "Corolla")
#print(persona1.presentarse())
#print(persona1.conducir())
#print(persona1.hacer_sonidos())

# Ejemplo 3 Composicion

class Persona:
    def __init__(self, nombre, vehiculo):
        self.nombre = nombre
        self.vehiculo = vehiculo

    def presentarse(self):
        return f"Me llamo {self.nombre} y conduzco un {self.vehiculo.marca} {self.vehiculo.modelo}"


vehiculo1 = Vehiculo("Toyota", "Corolla")    
persona2 = Persona("Juan", vehiculo1)
print(persona2.presentarse())
print(persona2.vehiculo.conducir())
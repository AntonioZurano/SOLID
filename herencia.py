class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"
    
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
    def describir(self):
        return f"Este automovil es un {self.marca} {self.modelo} con {self.puertas} puertas"    
    
class Camion(Automovil):
    def __init__(self, marca, modelo, puertas, carga):
        super().__init__(marca, modelo, puertas)
        self.carga = carga
    def describir(self):
        return f"Este camion es un {self.marca} {self.modelo} con {self.puertas} puertas y una capacidad de carga de {self.carga} kg"

# Instanciar un objeto de la clase Automovil
# y otro de la clase Camion
vehiculo1 = Automovil("Toyota", "Corolla", 4)
vehiculo2 = Camion("Ford", "F-150", 2, 2000)
print(vehiculo1.describir())
print(vehiculo2.describir())


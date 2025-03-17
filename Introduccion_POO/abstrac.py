class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._encendido = False
        self.velocidad = 0

    def mostrar_vehiculo(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

    def encender(self):
            self._encendido = True
            print("El vehículo ha sido encendido")
    
    def apagar(self):
            self._encendido = False
            print("El vehículo ha sido apagado")

    def acelerar(self, incremento):
        if self._encendido:
            self.velocidad += incremento
            print(f"La velocidad del vehículo es de {self.velocidad} km/h")
        else:
            print("El vehículo está apagado")

    def frenar(self, velocidad):
        if self._encendido:
            if self.velocidad - velocidad >= 0:
                self.velocidad -= velocidad
                print(f"La velocidad del vehículo es de {self.velocidad} km/h")
            else:
                print("La velocidad no puede ser negativa")
        else:
            print("El vehículo está apagado")


vehiculo1 = vehiculo("Toyota", "Corolla") 
vehiculo1.mostrar_vehiculo()
vehiculo1.encender()
vehiculo1.acelerar(50)
vehiculo1.frenar(20)
vehiculo1.apagar()
vehiculo1.acelerar(50)
vehiculo1.frenar(20)
vehiculo1.acelerar(50)
vehiculo1.encender()        
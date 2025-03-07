class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._encendido = False
        self.velocidad = 0

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
            self.velocidad -= velocidad
            print(f"La velocidad del vehículo es de {self.velocidad} km/h")
        else:
            print("El vehículo está apagado")

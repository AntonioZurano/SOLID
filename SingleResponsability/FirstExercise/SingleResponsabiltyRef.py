class Engine:
    def getRPM(self):
        return 3000 # valor por defecto del motor
    
class Vehicle:
    def __init__(self, name, speed, engine):
        self._name = name
        self._speed = speed
        self._engine = engine

    def getName(self):
        return self._name

    def getEngineRPM(self):
        return self._engine.getRPM()

    def getMaxSpeed(self):
        return self._speed

class VehiclePrinter:
    def __init__(self, vehicle):
        self._vehicle = vehicle

    def printInfo(self):
        print(
            "Vehicle: {} \nMax Speed: {} \nEngine RPM: {}".format(
                self._vehicle.getName(), 
                self._vehicle.getMaxSpeed(), 
                self._vehicle.getEngineRPM()
            )
        )
        
class VehiclePersistance:
    def __init__(self, vehicle, db):
        self._vehicle = vehicle
        self._persistance = db
        print("Hey, storing data! in", self._persistance)

if __name__ == "__main__":
    engine = Engine()
    vehicle = Vehicle(name="Car", engine=engine, speed=200)
    persistance = VehiclePersistance(vehicle=vehicle, db="Firebase")  # db is not used in this example
    printer = VehiclePrinter(vehicle=vehicle)
    printer.printInfo()
    
    # Output:
    # Vehicle: Car 
    # Max Speed: 200 
    # Engine RPM: 3000
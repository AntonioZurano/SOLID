class Engine:
    def __init__(self):
        pass

    def getRPM(self):
        return 3000
        
class Vehicle:
    def __init__(self, name, speed):
        self._name = name
        self._speed = speed
        self._engine = Engine()

    def getName(self):
        return self._name

    def getEngineRPM(self):
        return self._engine.getRPM()

    def getMaxSpeed(self):
        return self._speed
    
    def printInfo(self):
        print(
            "Vehicle: {} \nMax Speed: {} \nEngine RPM: {}".format(
                self.getName(), self.getMaxSpeed(), self.getEngineRPM()
            )
        )

if __name__ == "__main__":
    vehicle = Vehicle("Car", 200)
    vehicle.printInfo()
    
    # Output:
    # Vehicle: Car 
    # Max Speed: 200 
    # Engine RPM: 3000
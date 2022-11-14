## Inheritance
## Class Car 

class car:
    def __init__(self,windows,doors,engineType) -> None:   # this will initialze three attribute
        self.windows = windows
        self.doors   = doors
        self.engineType = engineType

    def Driving(self):
        print ("Car is used for driving")

    # Audi is inhering from class car
class Audi(car):
    def __init__(self, windows, doors, engineType,maxSpeed) -> None:
        super().__init__(windows, doors, engineType)                    # this attribute is coming from class car
        self.maxspeed = maxSpeed

    def SelfDriving(self):
        print("I Can Self Drive.")

audiQ7 = Audi(4,5,"Electric","450 KMPH")

print(audiQ7)
audiQ7.Driving()                        # Object of audi class has access to Driving method of car class ? Inheritance ....

print(dir(audiQ7))


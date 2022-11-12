# Classes
# constructors, attributes , methods

# Classes is a real world entity or objects which has its own attributes.
    #-attributes=properties of the class
    #-methods = actions of the class

class Car:
    pass

# we can create multiple copies of car class or object, car class is a blueprint

# Class object without consturtor
car1 =  Car()
car2 = Car()

car1.windows = 4
car1.tyres = 4
car1.engine = "diesel"

car2.windows = 6
car2.tyres = 6
car2.engine = 'petrol'

print(car1.engine)
print(car2.engine)
print(dir(car1))     # it will return all the default methods and attributes in the object which is visible this will also give
                    # many in built method eg.. __init__.

# Class with construtor
# __init__ : this method is called constuctor

class car:
    #Constructor
    def __init__(self,windows,tyres,engine):             # self is default
        self.windows = windows
        self.tyres = tyres
        self.engine = engine

    def EngineType(self):                       # Method of the class
        print("This car has {} engine".format(self.engine))

mycar = car(4,4,"Electric")                            # whenvever we initilize an object first thing called is constructor.
print(mycar.engine)
print("The total number of windows in my car is {}".format(mycar.windows))
mycar.EngineType()


#Can we have multiple consturctors in PYTHON????
    #Yes, we do can have multiple constructors in .net,c#. Multipe constructors should have different parameters.

class Animal:
    def __init__(self,name,speceis) -> None:
        self.name = name
        self.speceis = speceis
    
    def __init__(self,name,speceis,sound) -> None:
        self.name = name
        self.speceis = speceis
        self.sound = sound

    def MakeSound(self):
        print("This animal {} makes a sound of {}".format(self.name,self.sound))



cat = Animal("Kitty","Mammals")  # this results in run time error saying TypeError: Animal.__init__() missing 1 required positional argument: 'sound'
# What i can see is that the most latest constructor overrides the previous constuctor....!!!!!!

dog = Animal("Tommy","Mammals","Woof Wooof")
print(dog)
print(dog.name)
dog.MakeSound()

#------------------------- Lets Create Multiple Constructor in PYTHON ------------------------------



#Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that
#allows a class to inherit attributes and methods from another class. 

## ## Parent class
class Car:
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
    
    def drive(self):
        print(f"The person will drive the {self.enginetype} car ")
### child class
class Tesla(Car):     ## is supposed to call car class insider tesla and remeber all attributes
    def __init__(self,windows,doors,enginetype,is_selfdriving):        ### add all attributes from parent class along with new attrinute
        super().__init__(windows,doors,enginetype)         #### super() allows to bring the attributes which are required from parent class except self
        self.is_selfdriving=is_selfdriving                 ### add one more attribute self_driving in self

    def selfdriving(self):
        print(f"Tesla supports self driving : {self.is_selfdriving}")

tesla1=Tesla(4,5,"electric",True)
tesla1.selfdriving()

##Out: Tesla supports self driving : True



############## Multiple Inheritance
## When a class inherits from more than one base class.
## Base class 1
class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("Subclass must implement this method")

## BAse class 2
class Pet:
    def __init__(self, owner):
        self.owner = owner


##Derived class
class Dog(Animal,Pet):
    def __init__(self,name,owner):
        Animal.__init__(self,name)     ### Not using super() instead using animal bcz i have 2 classes here and particularly mention ing the class to refer to
        Pet.__init__(self,owner)

    def speak(self):
        return f"{self.name} say woof"
    

## Create an object
dog=Dog("Buddy","Krish")
print(dog.speak())
print(f"Owner:{dog.owner}")





###### Polymorphism
#Polymorphism is a core concept in Object-Oriented Programming (OOP) that allows objects of different 
#classes to be treated as objects of a common superclass. 
#It provides a way to perform a single action in different forms. 
#Polymorphism is typically achieved through method overriding and interfaces

#### Method Overriding
# Method overriding allows a child class to provide a specific implementation of a method 
# that is already defined in its parent class

## Base Class
class Animal:
    def speak(self):
        return "Sound of the animal"   
    
## Derived Class 1
class Dog(Animal):
    def speak(self):         ### class dog has inherited all attributes of class animal but defined its won function
        return "Woof!"
    
## Derived class
class Cat(Animal):
    def speak(self):          ### class cat has inherited all attributes of class animal but defined its won function
        return "Meow!"

dog=Dog()  
cat=Cat()
print(dog.speak())
print(cat.speak())

## Function that demonstrates polymorphism
def animal_speak(animal):
    print(animal.speak())
    
animal_speak(dog)


# Polymorphism with Abstract Base Classes
# Abstract Base Classes (ABCs) are used to define common methods for a group of related objects.
# They can enforce that derived classes implement particular methods, promoting consistency across different implementations.


from abc import ABC,abstractmethod

## Define an abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

## Derived class 1
class Car(Vehicle):
    def start_engine(self):
        return "Car enginer started"
    
## Derived class 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle enginer started"
    
# Function that demonstrates polymorphism
def start_vehicle(vehicle):
    print(vehicle.start_engine())

## create objects of cAr and Motorcycle

car = Car()
motorcycle = Motorcycle()

start_vehicle(car)    ### output: Car enginer started

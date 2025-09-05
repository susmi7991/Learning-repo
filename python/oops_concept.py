
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





########## Encapsulation
# Encapsulation is the concept of wrapping data (variables) and methods (functions) together as a single unit.
# It restricts direct access to some of the object's components, which is a means of preventing accidental interference
# and misuse of the data.
# public variable - Can be called outside the class.
# private variable- Can not be called outside the class. its completely hidden... 
# protected variabls - Can not be called outside the class but can be called from another derived class

### Encapsulation  with Getter and Setter MEthods
### Public,protected,private variables or access modifiers

class Person:
    def __init__(self,name,age):
        self.name=name    ## public variables
        self.age=age      ## public variables

def get_name(person):
    return person.name

person=Person("Krish",34)
get_name(person)

## private
class Person:
    def __init__(self,name,age,gender):
        self.__name=name    ## private variables
        self.__age=age      ## private variables
        self.gender=gender

def get_name(person):
    return person.__name

person=Person("Krish",34,"Male")
get_name(person)

### protected
class Person:
    def __init__(self,name,age,gender):
        self._name=name    ## protected variables
        self._age=age      ## protected variables
        self.gender=gender

class Employee(Person):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)


employee=Employee("KRish",34,"Male")
print(employee._name)


## Getter method helps me to get any private variable
## Setter method helps me to change any value, given to the private variable
## Encapsulation With Getter And Setter
class Person:
    def __init__(self,name,age):
        self.__name=name  ## Private access modifier or variable
        self.__age=age ## Private variable

    ## getter method for name
    def get_name(self):
        return self.__name
    
    ## setter method for name
    def set_name(self,name):
        self.__name=name

    # Getter method for age
    def get_age(self):
        return self.__age
    
    # Setter method for age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age cannot be negative.")


person=Person("Krish",34)

## Access and modify private variables using getter and setter

print(person.get_name())
print(person.get_age())

person.set_age(35)
print(person.get_age())

person.set_age(-5)
    



##### Abstraction
# Abstraction is the concept of hiding the complex implementation details and showing only the 
# necessary features of an object. This helps in reducing programming complexity and effort.

from abc import ABC,abstractmethod

## Abstract base cclass
class Vehicle(ABC):
    def drive(self):
        print("The vehicle is used for driving")

    @abstractmethod                     ##### Bsically abstract method is hiding all the methods defined inside the class except the function outside abstract
    def start_engine(self):
        pass

class Car(Vehicle):                        ##### Derived class can inherit the parent class methods but not the methods of abstract method.    
    def start_engine(self):                  #### To call the abstract methods we have to create another method in derived class
        print("Car enginer started")

def operate_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.drive()

car=Car()
operate_vehicle(car)




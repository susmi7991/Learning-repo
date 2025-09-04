#Classes and Objects
#Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and computer programs. 
#OOP allows for modeling real-world scenarios using classes and objects. 
#This lesson covers the basics of creating classes and objects, including instance variables and methods.


### Modeling a Bank Account

## Define a class for bank account
class BankAccount:
    ## constructor
    def __init__(self,owner,balance=0):     ## At initialization the balance was 0
        self.owner=owner                    # defining attributes
        self.balance=balance                # defining attributes

    def deposit(self,amount):                # defining instance methods
        self.balance+=amount
        print(f"{amount} is deposited. New balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds!")
        else:
            self.balance-=amount
            print(f"{amount} is withdrawn. New Balance is {self.balance}")

    def get_balance(self):
        return self.balance
    
## create an account

account=BankAccount("Krish",5000)
print(account.balance)


## Call isntance methods
account.deposit(100)
account.withdraw(300)
print(account.get_balance())

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






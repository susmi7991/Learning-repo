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






## Find even number
even = [x for x in range(51) if x % 2 == 0]
print("even_list:", even)
## Find odd number
odd = [x for x in range(51) if x % 2 != 0]
print("odd_list:", odd)
## find squares until 100
squares= [x**2 for x in range (101)]
print("squares:", squares)
## Find cubes
cubes= [x**3 for x in range (31)]
print("cubes:", cubes)
## Prime numbers
prime=[]
for num in range(1,101):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            prime.append(num)
print("prime:",prime) 
## fibonaci series
num1=int(input("Emter starting numer 1"))
num2=int(input("Emter starting numer 2"))
fib=[]
for i in range(11):
    sum = num1 + num2
    fib.append(sum)
    num1 = num2
    num2 = sum
    if i==10:
        break
print("fibonacci series:", fib)

### password creation
def is_strong_password(password):
    """This function checks if the password is strong or not"""
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+' for char in password):
        return False
    return True
print(is_strong_password("WeakPwd"))
print(is_strong_password("Str0ngPwd!"))

### temperature to ferhenheit
def convert_temperature(temp,unit):
    """This function converts temperature between Celsius and Fahrenheit"""
    if unit=='C':
        return temp * 9/5 + 32  ## Celsius To Fahrenheit
    elif unit=="F":
        return (temp-32)*5/9 ## Fahrenheit to celsius
    else:
        return None
print(convert_temperature(25,'C'))
print(convert_temperature(77,'F'))


#### shopping cart values
def calculate_total_cost(cart):
    total_cost=0
    for item in cart:
        total_cost+=item['price']* item['quantity']

    return total_cost
cart=[
    {'name':'Apple','price':0.5,'quantity':4},
    {'name':'Banana','price':0.3,'quantity':6},
    {'name':'Orange','price':0.7,'quantity':3}

]
total_cost=calculate_total_cost(cart)
print(total_cost)


import re

# Email validation function
def is_valid_email(email):
    """This function checks if the email is valid."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

print(is_valid_email("test@example.com"))  # Output: True
print(is_valid_email("invalid-email"))  # Output: False

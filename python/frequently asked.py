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

## calling the function
print(is_strong_password("WeakPwd"))
print(is_strong_password("Str0ngPwd!"))

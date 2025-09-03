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

#### list manipulation
misc =["Hello",3,6,3,"five",3.14,8]
misc.append("world")  # append adds at last
misc.insert(1,"World") #insert
misc.remove("world")  # delete
misc.pop()  # delete last element
misc[5]=6.7  ## updated 6th element "five"
misc.sort()  ## sorts ascending order cannnot sort misc because its combination of int and str
sorte_misc=sorted(misc,reverse="True")   # sorts in desc order cannnot sort misc because its combination of int and str
print(misc)
lst=[14,2,7,5,7,3]
lst.sort()
misc.append(lst)   ## appends misc elements and list of lst elements
misc_lst=[tuple(misc)+tuple(lst)]  ### Appends the elements of misc and lst
misc_lst

#### Tuples are fixed and cant be changed . usecase -used in uDFs
#### lists can be manipulated. Use case - frequetly changing variables list
## Tuple =() ||  List=[]  ||  set={} || dictionary={"key":"value"}

#set
my_set={1,2,3,4,5,6} # set([1,2,3])
my_set.add(20)
my_set.remove(20)  
my_set.pop()     #removes 1st element
set2={4,5,6,7,8}
my_set.union(set2)
my_set.intersection(set2)
print(set2.issubset(my_set))

## dictionary key value pair 

student={"name":"sus","age":28,"grade":24}
print(student.get('grade'))
print(student.get('name'))
student["age"]=33  ##update value for the key
student["address"]="India" ## added a new key and value
keys=student.keys() ##get all the keys
keys=student.values() ##get all the keys
for key,value in student.items():  # pulls all key values
    print(f"{key}:{value}")
## Nested Disctionaries
students={
    "student1":{"name":"sus","age":31},
    "student2":{"name":"rahul","age":35} }
### Merging of dictionaries
dict1={"a":1,"b":2}
dict2={"b":3,"c":4}
merged_dict={**dict1,**dict2}

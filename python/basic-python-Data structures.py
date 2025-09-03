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


### Functions:
def print_details(*args,**kwargs):
    for val in args:
        print(f" Positional arument :{val}")   
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_details(1,2,3,4,"Sus",name="Sus",age="28",country="India")
###Output
#  Positional arument :1
#  Positional arument :2
#  Positional arument :3
#  Positional arument :4
#  Positional arument :Sus
# name:Sus
# age:28
# country:India



## Lambda function
addition=lambda a,b:a+b  ## lambda itself is a definition of function
even1=lambda num:num%2==0
addition1=lambda x,y,z:x+y+z

numbers=[1,2,3,4,5,6]
lambda x:x**2 (square of x)
lst_sq=list(map(lambda x:x**2,numbers)) ## map()- applies a function to all items in a list

or
##########
def square(number):
    return number**
lsit_sq=[]
for number in numbers:
    square=number**2
    list_sq=list_sq.append(square)
#########


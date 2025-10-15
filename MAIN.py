import math
from collections import namedtuple
import sys
from datetime import datetime as dt
print("jesus is \u2764")
print(" \u2663")
'''
class Dog:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def Bark(self):
        print(f"{self.name} of {self.age}years old and height {self.height}meters says Woof!!")
name=input("What is your name?")
name_1=name.upper()
age=int(input("What is your age?"))
height=int(input("What is your height?"))
my_dog=Dog(name_1,age,height)

print(my_dog.name)
#my_dog.Bark()

def quadratic_equation():
    a = 0
    x=int(input("What is x?"))
    y=int(input("What is y?"))
    z=int(input("What is z?"))
    result=x*a+y
    result=z
    result=z-y
    result/=x
    a=result
    print(a)

#quadratic_equation()

def max_num():
    numbers=[1,23,63,765,2434,6322,32,25434,24,242389,90]
    numbers.sort()
    print(numbers[-1])

#max_num()

class Person:
    def __init__(self, P_name, P_age,color):
        self.P_name=P_name
        self.P_age=P_age
        self.color=color

    def __str__(self):
        return f"My name is {self.P_name},of age {self.P_age}, and color {self.color}"


the_person=Person("Habib",24,"fair")
print(the_person)
print(the_person.__str__())


print("Hope your name is"+" "+name+" "+"or"+" "+"its is"+" "+"Habib")

for i in range(1,6):
    print("I love you")

array=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
middle_num=len(array)//2
print(array[middle_num])

for i in range(len(array)):
    array[i]+=1
    if array[i]>middle_num:
        array[i]=middle_num
        print(array[i])
    else:
        array[i]=array[middle_num]
        print(array[i])

def Api():
    try:
      num=int(input("Enter a number"))
      print(num)
    except ValueError:
        print("Wrong Input Value")

Api()

drinks={"Champagne":8,"Dresses":9,"HouseholdEquip":12}
print(drinks)
print(drinks.keys())
print(drinks.values())
drinks["Juice"]=8
print(drinks.setdefault("Champagne",12))
print(drinks)
employee={"Nina":["Boyfriend","Husband","Monogamous"],"George":["Girlfriend","Wife","Polygamous"]}
print(employee)
employee.update({"Claire":["Husband","Wife","Polygamous"]})
print(employee)
print(employee.keys())
print(employee.get("juice"))
print(employee.values())
print(employee.items())


prices ={}
fruit=input("Enter fruit")
price=float(input("Enter price"))
prices[fruit]=price
print("the fruits are and price available are",prices)



allEmployeePrices= employee | prices
print(allEmployeePrices)


person={}
names=[person]
num_names=int(input("Enter a number\n"))
for i in range(num_names):
    name= input("Enter name")
    age=int(input("Enter age"))
    person[name]=age
    print(f"The names are{names}")
'''
eyes= "O"
nose ="."
mouth="-"
print(f"   {eyes*2}")
print(f"   {nose*2}")
print(f" {mouth*6}")

Car=namedtuple("Car",["model","color","price"])
Toyota=Car('Supra','blue',20000)
print(Toyota)
print(Toyota.price)

nums1=set([1,2,3,1,11,2,13,4,5])
nums2=set([1,2,3,4,5,6,7,8,9,1,11,2,13])
print(nums1)
nums1.add(12)
print(nums1)
nums1.intersection(nums2)
nums2.remove(11)
nums1.pop()
inter=set.intersection(nums1,nums2)
nums1.clear()
print(nums1)
nums2.intersection(nums1)
print(nums1)
print(nums2)
print(inter)
print(sys.version)
print(dt.now())


number1=3
number2=9
print(f"{number1:.3f}")
print(f"{number2:.3f}")
print(f"{number2:b}")

hello="Hello World"
print(hello.strip("H"))
print(hello.lstrip("Hello"))

print(hello.upper())
print()


    
class MyClass:
    x = 5


p1 = MyClass()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.name}({self.age})"

    def myfunc(self):
        print("Hello my name is " + self.name)


p2 = Person("John", 35)

print(p2)  # John(35)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))

for x in myiter:
    print(x)


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Mercedes", "SL63")
boat1 = Boat("Ibiza", "Touring20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

rpg = 123


def best_func():
    global rpg
    rpg = 100


import datetime

taym = datetime.datetime.now()

print(taym.year)
print(taym.strftime("%A"))

new_taym = datetime.datetime(2023, 8, 19)

maksimum = max(5, 10, 15)
minimum = min(5, 10, 15)
positive = abs(-6.5)
four_to_three = pow(4, 3)

import math

square_root = math.sqrt(4)
upper = math.ceil(1.4)
down = math.floor(1.4),
pay = math.pi

import json

x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)

person_info = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

pers_inf_js = json.dumps(person_info)

json.dumps(person_info, indent=4, seperators=(". ", "= "))
json.dumps(person_info, indent=4, sort_keys=True)

import re

txt1 = "The rain in Spain"
x1 = re.search("^The.*Spain$", txt1)

txt2 = "The rain in Spain"
x2 = re.findall("ai", txt2)

txt3 = "The rain in Spain"
x3 = re.findall("Portugal", txt3)

txt4 = "The rain in Spain"
x4 = re.search("\s", txt4)

print("The first white-space character is located in position:", x.start())

txt5 = "The rain in Spain"
x5 = re.split("\s", txt5)

txt6 = "The rain in Spain"
x6 = re.split("\s", txt6, 1)

txt7 = "The rain in Spain"
x7 = re.sub("\s", "9", txt7)

txt8 = "The rain in Spain"
x8 = re.sub("\s", "9", txt8, 2)

txt9 = "The rain in Spain"
x9 = re.search(r"\bS\w+", txt9)
print(x9.span())

txt10 = "The rain in Spain"
x10 = re.search(r"\bS\w+", txt10)
print(x10.string)

txt11 = "The rain in Spain"
x11 = re.search(r"\bS\w+", txt11)
print(x11.group())

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

num = -1

if num < 0:
  raise Exception("Sorry, no numbers below zero")

username = input("Enter username:")
print("Username is: " + username)

if not type(username) is str:
  raise TypeError("Only integers are allowed")

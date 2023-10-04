# This can be used to comment on one line

"""
This can be used for
multi-line comments
"""

integer1 = 1
float1 = 2.5
string1 = "Hello World!"
boolean1 = True

print(type(integer1))
print(type(float1))
print(type(string1))
print(type(boolean1))

string2, string3, string4 = "Orange", "Lemon", "Mint"

print(string2)
print(string3)
print(string4)

string5 = string6 = string7 = "Apple"

print(string5)
print(string6)
print(string7)

fruits = ["apple", "banana", "cherry"]
string8, string9, string10 = fruits

print(string8)
print(string9)
print(string10)

print(string8, string9, string10)
print(string1 + string2 + string3)  # An error occurs if it used with different variable types.

global integer2  # To create a global variable inside a function or loop
integer2 = 8

float2 = 2.6
float3 = 2.4

integer3 = int(float2)
integer4 = int(float3)
print(integer3)
print(integer4)

print(35e3)  # e is used as power of 10
print(type(35e3))

len(string3)  # used to find the length of the variable

quantity = 3
itemno = 567
price = 49.95
myorder1 = "I want {} pieces of item {} for {} dollars."
print(myorder1.format(quantity, itemno, price))

myorder2 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder2.format(quantity, itemno, price))

print(string1 + "\n\t" + string2)

string11 = "Hello lololo"
string12 = "World!"
string13 = "Hello lololo \rWorld!"
print(string11)

# string1 = "Hello World!"
print(string1.casefold())
print(string1.center(40, "O"))  # The character must be exactly one character long
print(string1.center(40))

list1 = ["apple", "banana", "orange"]
string = "0l0".join(list1)
print(string)

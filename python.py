print("Hello World!")

# to give information about your code
# there is comment lines in Python

day_of_week = 5
type(day_of_week)  # integer

pi = 3.14
type(pi)  # float

bmi_read = "body mass index"
type(bmi_read)  # string

z = True
type(z)  # boolean

str(day_of_week)  # conversion to string
float(day_of_week)  # conversion to float
int(z)  # conversion to integer
bool(0)  # conversion to boolean

# different types of list
fam_heights = [1.65, 1.80, 1.75, 1.64, 1.68]

fam_random = ["Ruveyda", 1.80, True, 25]

members_heights = [["Ruveyda", 1.68],
                   ["Ubeydullah", 1.80],
                   ["Humeyra", 1.65],
                   ["Fatma", 1.64],
                   ["Mustafa", 1.75]]

# index of list, slicing and dicing
print(fam_heights[2])  # index
print(fam_heights[-3])

print(fam_heights[0:3])  # slicing
print(fam_heights[:3])
print(fam_heights[-4:])

fam_heights[0] = 1.76  # replacing list elements

fam_heights += [1.60]  # extending a list

del(fam_heights[-1])  # deleting an element from a list

# important about memory
list1 = [1, 2, 3, 4]
list2 = list1

"""
if we make an assignment like the above every change
in any list effect the other one. If we want to have
a list just like the other one but independent one
we should do it like the below.
"""

list3 = list(list1)
list4 = list1[:]

# some built-in functions
len(list1)  # gives the num of elements in the list or string
help(print)  # gives information about the structure of any built-in function

list5 = sorted(list1)  # a copy of the list in ascending order
list6 = sorted(list1, reverse=True)  # a copy of the list in ascending order

# string methods
bmi_read.upper()  # capitalizes letters
bmi_read.count('b')  # counts the number of 'b'

# list methods
list1.index("2")  # finds the index of element
list1.count(5)
list1.append(3)  # adds the element to end of the list
list1.remove(1)  # removes the element
list1.reverse()  # edits the list from last to first

# importing a package
import numpy as np

from numpy import array  # selective import

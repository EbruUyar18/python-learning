#range

print(range(0,50))
print(list(range(10)))

my_list=[10,20,30,40,50,60]
for num in my_list:
    print(num*2)

print(list(range(5,20,2)))
for ix in range(len(my_list)):
    print(ix)

for ix in range(len(my_list)):
    print(my_list[ix])
    print()

#enumerate

for element in enumerate(my_list):
    print(element)

for (ix,value) in enumerate(my_list):
    print(ix)
print()

#random

from random import randint
print(randint(0,100))
"""
from random import shuffle
my_list2=[11,12,13,14]
print(shuffle(my_list2))
"""
randint(0,len(my_list))
my_list[randint(0,len(my_list)-1)]

#zip

name_list=["ebru","betul","elif"]
surname_list=["uyar","gurleyen","giray"]
age_list=[20,20,21]
zippedList=list(zip(name_list,surname_list,age_list))
print()
print(zippedList)
print()

new_list=[]
my_string="metallica"
for element in my_string:
    new_list.append(element)
print()
print(new_list)
print()

#list comprehension
new_list2=[]
new_list2=[element for element in my_string]
print(new_list2)
print()

number_list=[10,20,30,40,50]
new_number_list=[]
new_number_list=[num/2 for num in number_list]
print(new_number_list)
#or
new_number_list2=[]
for num in number_list:
    new_number_list2.append(num/2)
print(new_number_list2)
    
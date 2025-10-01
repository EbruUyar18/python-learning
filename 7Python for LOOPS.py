#for LOOPS
my_list=[10,20,30,40,50,60,70,80]
print(my_list[0]/5*2)

#or

for number in my_list:
    print(number)
    print(number/5*2)
    
print("for loop started")
for x in my_list:
    newNumber=x/5*2
    print(newNumber)
print("for loop ended")

for num in my_list:
    if num%6==0:
        print(num)
    else:
        print("*_*")

myName="Ebru Uyar"
for letter in myName:
    print(letter)

newTuple=(10,20,30,40,50)
for num in newTuple:
    print(num/5*2)


newList=[("a","b"),("c","d"),("e","f"),("g","h")]
for element in newList:
    print(element)

#tuple unbacking

for (x,y) in newList:
    print(y)

myTuple=[(0,1,2),(3,4,5),(6,7,8)]
for (x,y,z) in myTuple:
    print(z)

mySet={1,2,3,4,5}
for num in mySet:
    print(num)
    
my_dict={"k1":10,"k2":11,"k3":12}
for element in my_dict:
    print(element)
my_dict.items()

for (key,value) in my_dict.items():
    print(key)
for num in my_dict.values():
    print(num)

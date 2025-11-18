#practical fuctions

def diviceNumber(num):
    return num/2
diviceNumber(20)

myList=[1,3,5,7,9]
myList_result=[]
for number in myList:
    myList_result.append(diviceNumber(number))
print(myList_result)

#help(map)
"""
map kısayolu yukarıdaki for döngüsü ile aynı işlemi yapar !!!
"""
print()

map(diviceNumber,myList)
print(list(map(diviceNumber, myList)))

def controls(string):
    return "Ebru" in string
print(controls("Ebru Uyar"))
print(controls("uyr"))

myString_list=["Ebru","Ebru uyar","Uyar","uyar Ebru"]
print(list(map(controls, myString_list)))
print()
#FILTER

print(list(filter(controls, myString_list)),"\n")

#LAMBDA

multiplyLambda= lambda num:num*3
print(type(multiplyLambda),"\n")
print(multiplyLambda(20))
result=multiplyLambda(10)
print(result,"\n")
numList=[10,20,30,40]
print(list(map(lambda num: num/4, numList)))

#Scope

x=20
def multiply(num):
    x=5
    return num*x
print(multiply(11),"\n")
print(x)


#LEGB (Local,Enclosing,Global, Built-i-In)

myString="Ebru" #global
def myfunc():
    myString="Ebru2"
    print(myString)
    def myfunc2():
        myString="Ebru3"
        print(myString)
    myfunc2()
print(myString)
myfunc()

print(myString,"\n")

def test1():
    myVeriable=10
    print(myVeriable*2,"\n")
    
def test2():
    print(myVeriable*3)
test1()
#test2() içinde myVeriable isimli bir değişken tanımlı olmadığıdan error verir


y=2
def myFunction(y):
    print(y)
    y=5
    
    print(y,"\n")
    return y
myFunction(10)
print(y,"\n")

def changeY():
    global y
    y=5
    print(y)
changeY()
#FUNCTİONS
def printf():
    print("hello function")
printf()

def function(x):
    print(x)
print(function(10))
print(function("ebru"))


def Q(name):
    print(name)
Q("ebru")

def names(x,y,z):
    print(x)
    print(y)
    print(z)

def fullName(name,surname):
    print(name+surname)
fullName("Ebru"," Uyar" )

def fullName2(name,surname="Uyar"):
    print(name+surname)
fullName2("ebru ")
fullName2("ebru ","Uyar2")
print()
#RETURN FUNCTİON

def summation(num1,num2,num3):
    print(num1+num2+num3)
summation(10, 2, 8)
print()
x=summation(10, 2, 8)
print()
print(x)
print()
print(type(x))

def return_summation(num1,num2,num3):
    return num1+num2+num3

w=return_summation(10, 20, 30)
print(w)

def controls(a):
    if a[0]=="a":
        return "a"
        
    else:
        print(":(")

print(controls("ebru"))
print() 
print(controls("uyar"))
print()  
print(controls("ali"))
print()
print(controls("ayşe"))


#args,kwargs
"""
def args_sum(num1,num2,num3):
    return sum(num1+num2+num3)
"""
def args_sum(*args):
    return sum(args)
print()
print(args_sum(10,20,30,40))
    
def args_example(*args):
    print(args)
args_example(1,2,3,4,5,6,7,8,9)

def kwargs_example(**kwargs):
    print(kwargs)

kwargs_example(apple=10,banana=20,kiwi=15)

def kwargs_example2(**kwargs):
    if "apple" in kwargs:
        print("It  has")
    else:
        print("It hasn't")
        
kwargs_example2(apple=10)
print(kwargs_example2(apple=10))
print(kwargs_example2(banana=20,kiwi=15))

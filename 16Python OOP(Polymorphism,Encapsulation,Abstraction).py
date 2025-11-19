#POLYMORPHİSM 
class Fruit():
    def __init__(self,name):
        self.name=name
    def info(self):
        return f"100 calories {self.name}\n"

banana=Fruit("Banana")
apple=Fruit("Apple")

print(banana.info())
print(apple.info(),"\n")

# alternatif kullanım şekli

fruitList=[banana,apple]

for fruit in fruitList:
    print(fruit.info())
    #aynı ismi kullanarak farklı ögelerin değerlerine erişebiliyoruz

#ENCAPSULATİON (hapsetmek, erişebilirlik)

class Object():
    def __init__(self,name,size):
        self.name=name
        self.__size=size #bu değişkenin değeri değiştirilemez hale geldi
    def info(self):
        print(f"{self.name} size is:{self.__size} cm\n")
        
    #size değişkenini değiştirmek için fonk tanımı
    def changeSize(self,size):
        self.__size=size

desk=Object("desk", 100)
desk.info()

bed=Object("bed",120)
print(bed.info())

desk.changeSize(150)
print(desk.info())


#ABSTRACTİON (soyutlama)

from abc import ABC ,abstractmethod

class Car(ABC):
    @abstractmethod
    def maxSpeed(self):
        pass
    

#myCar=Car() error verir
#Abstract sınıftan nesne oluşturulamaz

class Tesla(Car):
    def maxSpeed(self):
        print("200 km")
        
myTesla=Tesla()
myTesla.maxSpeed()


class Name():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"{self.name}:{self.age}"
    
    def __len__(self):
        return self.age
    
myName=Name("Ebru", 20)
myfriendName=Name("Betul", 20)

print("\n\n")
print(myName.name)
print(len(myName))
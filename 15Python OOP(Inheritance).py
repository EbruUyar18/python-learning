class Animals():
    year=7
    def __init__(self,age):
        self.age=age
    
        self.animalHumanAge=age*self.year #methoda ihtiyaç duyulmadan  bu yapılabilir
        """
            Her obje çağırıldığında çalışacak olan method budur ve
            bu fonksiyon altında her şey yapılabilir.
        """
    def HumanAge(self):
        return self.age*Animals.year # 'Animals.year' or 'self.year' use
    
myDog=Animals(4)
#ikisi de aynı çıktıyı verecek
print(myDog.HumanAge()) 
print(myDog.animalHumanAge,"\n\n")

#INHERITANCE kalıtım almak

class Department():
    def __init__(self,depName):
        self.name=depName
        print("\n")
        
    #Method
    def sector(self):
        print("Sector isn't know")
    #Method
    def sector2(self):
        print("Sector is know")
        
    
Person1=Department("Computer Engineer")
print(Person1.name,"\n\n")
print(Person1.sector2())

Person2=Department("empty")
print(Person2.name,"\n\n")
print(Person2.sector())

#Department class'ından kalıtım alma işlemi
class Department2():
    def __init__(self,depName):
        Department.__init__(self, depName)
        print("\n")
        """
             Sadece init fonksiyolarının aynı olması kalıtım almak
             için yeterlidir.Bu şekilde kalıtımı kullanılabilir hale getiririz.
        """
        
    #Kalıtım alınan classta yeni method atamaları yapılabilir.
    def sector3(self):
        print("Sector is pravite")

Person3=Department2("Private")
print(Person3.sector3())

#override(üstüne yazma)

def test1(self):
    print("XXX")
print(Person1.test1)
print(Person2.test1)

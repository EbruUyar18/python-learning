class Person():
    name=" "
    age=0
    gender=" "
    job="Doctor"
    birthday=0
    #method, initializer
    def __init__(self,nameInput,ageInput,genderInput):
        self.name=nameInput
        self.age=ageInput
        self.gender=genderInput
        """ 
            Burada classtan nesne kalıtımı almak için self anahtar kelimesini kullanmalıyız
            self anahtar kelimesini kullanmadığımız taktirde kalıtım yapamayız.
            init içine aldığımız değişkenlerin değeri giririlmek zorundadır. job ve birthday
            değişkenlerine değer ataması yapmak zorunda değiliz.
        """
ebru=Person("Ebru",20,"Famale")
ebru.birthday="18 February 2005"
print(ebru.name)
print(ebru.age)
print(ebru.gender)
print(ebru.birthday)
print(ebru.job,"\n") 



#alternatif kodlama 

class Student():
    name=" "
    age=0
    gender=" "
    job=" "
    birthday=0
    
    # initalizer method
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
        # method
    def printName(self):
        print(self.name) 

#nesneler oluşturuluyor ve atama yapılıyor
student1=Student("Ebru", 20, "Female")
student2=Student("Betül",20,"Female")
student3=Student("Ali",19,"Male")
student3.job="Student"

stundent4=Student("Ahmet", 17, "Male")
stundent4.printName()

print("\nstudent1 is name",student1.name)
print("student2 is age",student2.age)
print("student3 is gender",student3.gender)
print("student3 is job",student3.job)
        


"""
CLASSTAN REFERANS ALMAK İÇİN self KULLANMAK ZORUNDAYIZ
"""



















myName="Ebru uyar"
#str türündeki değişkenin uzunluğunu verir
print(len(myName))

#str türündeki değişkenin son indeksini verir
myName[len(myName)-1]
myName[-1]

#str türündeki değişkenin indekslerine erişim
#myName[starting index,stopping index, stepping index]
myName[0:3]
myName[::2]

#değişkende aranan değerin yerini verir
myName.index("a")

#değişkeni bölmek için kullanılır
myName.split("a")

#değişkenin türünü belirlemek için
myFav="computer"
type(myFav)

myAge=20
type(myAge)

#MY SET EXAMPLES
"union elements, unordered"

myList=[10,11,11,13,12,12,14,15,15]
print(len(myList))
mySet=set(myList)

mySet2={10,11,11,13,12,12,14,15,15}
print()
print(mySet2)
mySet2.add(10)
mySet2.add(16)
mySet2.add(17)
mySet2.add(18)
mySet2.add(12)
print(mySet2)

mySet.union(mySet2) #union sets (setleri birleştirmek için)
mySet.intersection(mySet2) #intersection sets (ortak elemanları bulmak için)

countryList=["Turkiye","USA","UK","Turkiye","USA","France","Turkiye"]
len(set(countryList))

emptyList=[]
emptyList.append(10)
emptyList.append(12)
emptyList.append(14)


emptySet={}
type(emptySet)
emptySet1=set()
emptySet1.add(15)
print(emptySet1)

emptyList=list()

emptyDict=dict()
emptyDict["A"]=10
emptyDict["B"]=11
print(emptyDict)

#MY TUPLE EXAMPLES

"""
mytuple[0]=100 syntax error , immutability
"""
myTuple=["ebru","uyar"]

#BOOLEAN

print(5>1)
print(13<10)

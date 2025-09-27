#MY LİST EXAMPLES

floatlist=[3.14,18.02,20.05]
print(type(floatlist[0]))

mixlist=["Ebru",18.02,2025]
print(type(mixlist))

list1=[10,11,12]
list2=[13,14,15]
list1+list2
print(list2*2+list1*4)

print(type(mixlist[0]))

newList=["Ebru", "Uyar", [18,2,2005], "sophomore computer engineer",2]
birtdayList=newList[2]
print(birtdayList)
print(newList[2][0])
print(newList[:3:])

#MY DİCTİONARY EXAMPLES

"key-value pairing"


myİnformation={"name":"Ebru","surname":"Uyar", "age":20,"gender":"F"}
print(type(myİnformation))
print(myİnformation["age"])

print(myİnformation.keys()) #output keys
print(myİnformation.values()) #output values
list(myİnformation.values())
myİnformation["age"]=21

myİnformation.get("age",0)

myNEWdict={"a":"A","b":"B","c":"C"}
my_dict={10:"A",11:"B",12:"C"}
last_dict={"k1":10,"k2":11,"k3":[12,13,14],"k4":{"A":10,"B":11,"C":12}}

print(last_dict["k3"][1])
print(last_dict["k4"]["B"])

# name = input("Enter ur name")#prompt param in input
# age = input("Enter ur Age")
# print("Hi "+name +" of "+age+" years")

# n1 = input("enter a float or int num:")
# n2 = input("enter an only int num:")
# sum = float(n1) + int(n2)
# print(sum)

anList = ["an","list",4,True,False,"list"]
print(anList)
print(anList[-1])
print(anList[2:4])
print(str(anList[1])[3])
anList[3]="HEY"
print(anList)
anList2=[88,34]
anList.extend(anList2)
anList.append("last one")
anList.insert(3,"elem at index 3")
anList.remove(False)
anList.pop()
print(anList)
print(anList.index("list"))
print(anList.count("list"))
anList2.sort()
print(anList2)
anList.reverse()
print(anList)
anList3 = anList.copy()
anList.clear()
print(anList)
print(anList3)



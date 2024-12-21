#python list
#Lists are used to store multiple items in a single variable.
Mylist=["Apple","Mango","Banana","Guava",20,"30","Minhaz"]
print(Mylist)
##find length
print(len(Mylist))
#access list items,,list item start with zeo index
print(Mylist[1])

#negative indexing means it will start from ends
print(Mylist[-3])

#ranges of indexxs
print(Mylist[2:4])

#check item  exist in list
if "apple" in Mylist:
  print("Yes,Its exists")
else:
  print("No,this is not exist")

#change list items
Mylist[2]="Google"
print(Mylist)

#change range of list
Mylist[3:5]=["Facebook","Instagram","Twitter"]
print(Mylist)

#insert
Mylist.insert(5,"YOUTUBE")
print(Mylist)

#APPEND mEthod ,this will append in the last of the list
Mylist.append("Pinterest")

#remove items from the list
Mylist.remove("Google")
print(Mylist)
#remove by index
Mylist.pop(0)

print(Mylist)
#del also used for remove
del Mylist[0]
print(Mylist)

#Lopp through in list

#print all one by one

for x in Mylist:
  print(x)

  #print index number
  for i in range(len(Mylist)):
    print(Mylist[i])
#print one by one by while lopp
i=0
while i<len(Mylist):
 print(Mylist[i])
 i=i+1

 #list comprehension
 # new_list = [expression for item in iterable if condition]
Numberlist=[1,2,3,4,5]
new_list=[x*2 for x in Numberlist]
print(new_list)

#sort ;list
#use sort method this will sort  alphabetically or numerically according to list types
Mylist.sort()
print(Mylist)
#sort in descending order,To sort descending, use the keyword argument reverse = True:
Mylist.sort(reverse=True)
print(Mylist)

#copy a list
mynewList=Mylist.copy()
print(mynewList)

#join list items into a string
MynumList=[1,3,5,5,6]
for x in MynumList:
  Mylist.append(MynumList)
  print(Mylist)

#tuples
mytuple =("apple", "banana", "cherry")
print(type(mytuple))

#access tuple items
print(mytuple[1:2])#index 1 to 2
#index 0 items
print(mytuple[0])
#we cant change tyuple item directly,we have to convert this tuple to list and then convert this list and tuple and print this updated tuple
updateTuple=list(mytuple)
updateTuple.append("Minhaz")#will add in the last
updateTuple[1]="Uddin"
print(updateTuple)
myNewTuple=tuple(updateTuple)
print(myNewTuple)
#loop in tuple
for x in myNewTuple:
  print(x)
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

  

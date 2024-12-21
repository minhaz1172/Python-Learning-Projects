#python sets
Myset={"Minhaz","Mahin",1,4,7,"3","Marof"}
print(Myset)

#access items
for i in Myset:
  print(i)

#add items
Myset.add("Orange")
print(Myset)

#add sets
MynewSet={"HI","Youtube","tIKTOK"}
Myset.update(MynewSet)
print(Myset)

#add any list tuple set

#add list
myList=["tABNINE","cHATGPT","gEMINI"]
Myset.update(myList)
print(Myset)

#remove item from set by pop,remove discard method

#python dictonaries

myDict = {
    "Minhaz": {
        "Name": "Minhaz Uddin",
        "Age": int(12),
        "University": "RUET"
    }
}

print(myDict["Minhaz"])
print(myDict["Minhaz"]["Name"])
print(myDict["Minhaz"]["University"])

#accesing items
x=myDict["Minhaz"]["Age"]
print(x)
x=myDict.keys() #what keys in dictionary
print(x)

#update dictionary
myDict.update({"Age":int(23)})
print(myDict)
# add items to dictionary
myDict["profession"]="programmer"
print(myDict)

#loop in duictionary
for x in myDict:
  print(x)
 
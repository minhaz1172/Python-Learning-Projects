

#writing into file //if this file exist this will overwritten
file=open("D:\Python\Python-Learning-Projects\Zero_To_Advace\Python File\File1.txt","w")
file.write("Hello,writing into python file by write() mode")
file.close()

#reading a python file
file=open("D:\Python\Python-Learning-Projects\Zero_To_Advace\Python File\File1.txt","r")
content=file.read()
print(content)
print(type(content))
file.close()
#if the file dont exist this will create file automatically by append mode
#using with
with open("file2.txt","a") as file:
  file.write("This is the line appendded to this file by python i/o")
  print("Content appended successfully")

  #read line by line
file=open("D:\Python\Python-Learning-Projects\Zero_To_Advace\Python File\File1.txt","r")
line1=file.readline()
print(line1)
print("line1 printd")
  

# w+ used for both reading and writing
with open("File3.txt","w+") as f:
 f.write("This is opening and writing by w+ mode")
f.close()

# a+ mode use to append ,,if the file doesnot exist it will crearte and write
file1=open("file4.txt","a+")
file1.write("Today ia am going to cox's bazar for travelling .\n i will stay there for two days it is my first visit ")
file.close()


with open("file4.txt","r") as f:
 data=f.read()
 print("the content in the file4 is:",data)
 f.close()
 
#LOCAL SCOPE
def myfunc():
  x=200
  print(x)
myfunc()
 
 #global scope

x=300 #x is global
def myfunc():
  x=3400 #same variable but local
  print(x) #first execute local
myfunc()
print(x) #access global varibale 

#global keyword
x=300
def func():
  global x
  x=390

func()
print(x) #as we defined a variable as global,,this wil print global keyword variable


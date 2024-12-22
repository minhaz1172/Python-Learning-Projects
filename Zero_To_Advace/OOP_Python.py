# Normal class and objects
class Programmer:
    
    def __init__(self, name, language, age, home):
        self.name = name
        self.language = language
        self.age = age
        self.home = home

    def update(self,new_language,new_name):
        self.language =  new_language
        self.name = new_name
                
        
# Creating an object of the Programm er class
man = Programmer("Minhaz", "Python", 23, "Ctg")

# Printing the details of the programmer
print(f"The details of the programmer are: {man.name}, {man.language}, {man.age}, {man.home}")

# Updating the details of the programmer
man.update("Java","Minhaz")
print(f"the update name is:{man.name},{man.language}")
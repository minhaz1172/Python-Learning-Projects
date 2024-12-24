#python math module
import math
print(math.sqrt(4))
print(math.factorial(4))

#renaming python module

import math as mt
print(mt.pi)
print(mt.radians)

#python date module
import datetime
from datetime import date
import time
print(time.time())

#import a module from creation
# Import the custom module
import module1 as mi

# Taking user input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Using the module's functions and printing in one line
print(f"The results are: Addition={mi.add(a, b)}, Subtraction={mi.sub(a, b)}, Multiplication={mi.mul(a, b)}, Division={mi.div(a, b)}")

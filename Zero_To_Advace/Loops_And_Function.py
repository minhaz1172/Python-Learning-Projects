# For Loop
Name = ["Minhaz", "Uddin", "RUET", "ECE"]

# Print elements of the list
for i in Name:
    print(i)

# Print elements using range and index
for x in range(len(Name)):
    print(Name[x])

# Print numbers in a range
for k in range(1, 10):
    print(k)

# While Loop
count = 0
while count < 3:
    count += 1
    print("Minhaz Uddin")

# Break and Continue
# Break in for loop
for i in range(12):
    if i == 10:
        break
    print("5 x", i + 1, "=", 5 * (i + 1))
print("Out of loop")

# Break in while loop
i = 0
while i <= 12:
    if i == 10:
        break
    print("5 x", i + 1, "=", 5 * (i + 1))
    i += 1
print("Out of loop")

# Continue in for loop   ,,it is used to skiip iteration
for i in range(12):
    if i == 10:
        print("Iteration skipped for i=10")
        continue
    print("5 x", i + 1, "=", 5 * (i + 1))

#functions in python
#cheking a number is even or odd

def evenodd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

number = int(input("Enter a number: "))  # Convert input to integer
evenodd(number)

#factorial in python
def factorial(number):
    if number==0:
        return 1
    else:
        return number*factorial(number-1)

   
n=int(input("Enter a number"))
print(factorial(n))

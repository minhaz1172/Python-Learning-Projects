import json

# Correct JSON string
employee = '{"id": 1, "name": "Minhaz", "department": "Accounting", "state": "Dhaka", "under": ["Miraz", "Mizu", "Hasan", "Amid", "Jabed"]}'

# Converting JSON string to Python dictionary
print("This is JSON:", type(employee))

print("\nNow Convert JSON to Python dict:")
employee_dict = json.loads(employee)

print(type(employee_dict))  # Output: <class 'dict'>

# Now print the Python dictionary
print(employee_dict)

#convert python object to json'
#Here json.dumps() function will convert a subset of Python objects into a JSON string.

json_employee=json.dumps(employee_dict)

print("\nThis is JSON object:", type(json_employee))
print(json_employee)


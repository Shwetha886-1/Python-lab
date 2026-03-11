# Experiment-06
# Dictionary Operations

# Creating a dictionary
student = {
    "name": "Shwetha",
    "age": 20,
    "course": "BCA"
}

print("Original dictionary:", student)

# Accessing dictionary elements
print("Name:", student["name"])
print("Age:", student.get("age"))

# Adding element
student["marks"] = 90
print("After adding marks:", student)

# Updating value
student["age"] = 21
print("After updating age:", student)

# Removing element using pop()
student.pop("age")
print("After pop(age):", student)

# Removing element using del
del student["marks"]
print("After deleting marks:", student)

# Clear dictionary
student.clear()
print("After clear():", student)

# Dictionary methods
student = {"name": "Shwetha", "age": 20, "marks": 90}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Update dictionary
student.update({"marks": 95})
print("After update:", student)

# Iterating dictionary
print("Iterating dictionary:")
for key in student:
    print(key, ":", student[key])

# Nested dictionary
students = {
    "S1": {"name": "Ram", "marks": 90},
    "S2": {"name": "Riya", "marks": 80}
}

print("Nested dictionary access:", students["S1"]["name"])
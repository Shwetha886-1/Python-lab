# Creating a tuple
numbers = (10, 20, 30, 40, 50, 50)
print("Tuple elements:", numbers)

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Length of tuple
print("Length of tuple:", len(numbers))

# Count function
print("Count of 20:", numbers.count(20))

# Index function
print("Index of 30:", numbers.index(30))

# Tuple Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("Concatenated tuple:", combined)

# Tuple repetition
repeat_tuple = tuple1 * 3
print("Repeated tuple:", repeat_tuple)

# Membership check
print("Is 40 in numbers?", 40 in numbers)

# Iteration through tuple
print("Iteration through tuple:")
for num in numbers:
    print(num)

# Student Grade Calculator
def stud_grade():
    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    return name, grade

name, grade = stud_grade()
print("Student name:", name)
print("Grade:", grade)
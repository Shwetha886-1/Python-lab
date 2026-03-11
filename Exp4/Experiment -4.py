# Experiment -04
# List operations

# Creating List
kami = ["Akash", "Vikash", "Sakaham"]
team2 = ["Shreya", "Sneha", "Sahana"]

print(kami[0])
print(team2[-1])

# Slicing
a = [1,2,3,4,5,6,7,8,9]
e = a[1:8:2]
print(e)

# Append
my_group = [1,2,3]
my_group.append(4)
print(my_group)

# Copy
my_group = [1,2,3,4]
mex = my_group.copy()
print(mex)

# Traversing list using loop
place = ["delhi", "mumbai", "karnataka", "kerala"]
for i in place:
    print(i)

# Function example
def add_numbers(num1, num2):
    sum_result = num1 + num2
    print("The sum is:", sum_result)

add_numbers(5,4)

# Append and Remove
p = [10,20,30]
p.append(40)
print(p)

p.remove(10)
print(p)

# Extend
group1 = [1,2,3]
group2 = [4,5,6]
group1.extend(group2)
print(group1)

# Index
scores = [190,200,300,370,400,436,520]
score_index = scores.index(400)
print(score_index)

# Insert
marks = [190,200,300,400,436,520]
marks.insert(2,250)
print(marks)

# Sort
Score = [300,370,190,400]
Score.sort()
print("Ascending order:", Score)

Score.sort(reverse=True)
print("Descending order:", Score)
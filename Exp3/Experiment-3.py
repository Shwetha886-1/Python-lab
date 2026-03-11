# Experiment-03
# Write a program to implement string functions

# 1. Find length of string
S = input("Enter a string: ")
length = len(S)
print("Length of the string:", length)

# 2. Convert to Uppercase
S = input("Enter a string: ")
print("Uppercase:", S.upper())

# 3. Convert to Lowercase
S = input("Enter a string: ")
print("Lowercase:", S.lower())

# 4. Reverse a string
S = input("Enter a string: ")
print("Reversed string:", S[::-1])

# 5. Concatenate two strings
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
result = s1 + " " + s2
print("Concatenated string:", result)

# 6. Compare two strings
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if s1 == s2:
    print("Strings are equal")
else:
    print("Strings are not equal")

# 7. Check substring
S = input("Enter main string: ")
sub = input("Enter substring: ")
if sub in S:
    print("Substring found")
else:
    print("Substring not found")
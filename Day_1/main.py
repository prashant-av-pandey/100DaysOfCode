# Day 1 - Python Basics
# Topics: Printing, Commenting, Debugging, String Manipulation, Variables

# -------------------------
# Printing
# -------------------------
print("Hello, World!")
print("Welcome to Day 1 of 100 Days of Code")

# -------------------------
# Variables
# -------------------------
name = "Prashant"
age = 22
is_student = True

print("Name:", name)
print("Age:", age)
print("Student:", is_student)

# -------------------------
# String Manipulation
# -------------------------
greeting = "Hello"
message = greeting + ", " + name + "!"

print(message)
print(message.upper())     # Convert to uppercase
print(message.lower())     # Convert to lowercase
print(message.replace("Hello", "Hi"))

# -------------------------
# Commenting
# -------------------------
# This is a single-line comment

"""
This is a multi-line comment
used to explain larger blocks of code
"""

# -------------------------
# Debugging
# -------------------------
# Example of debugging by fixing an error

# Incorrect code (commented to avoid error)
# print("My age is " + age)  # TypeError

# Correct code
print("My age is", age)
print(f"My age is {age}")   # Using f-string

# -------------------------
# End of Day 1
# -------------------------
print("Day 1 completed successfully! 🚀")

# Python Learning Guide

Welcome to the **Python Learning Guide**! This document provides simple Python code examples along with notes to help you understand key concepts.

## 📌 Getting Started with Python

### 1. **Hello, World!**
```python
# This is the first program every beginner writes
print("Hello, World!")  # Prints text to the console
```
**Note:** `print()` is used to display output in Python.

### 2. **Variables and Data Types**
```python
# Variables store data values
name = "Alice"          # String
age = 25                # Integer
height = 5.4            # Float
is_student = True       # Boolean

print(name, age, height, is_student)
```
**Note:** Python is dynamically typed, meaning you don't need to declare variable types explicitly.

### 3. **Conditional Statements**
```python
# Decision-making with if-else
score = 85

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
else:
    print("Needs Improvement")
```
**Note:** Indentation is critical in Python to define code blocks.

### 4. **Loops (for & while)**
```python
# Using a for loop
for i in range(5):
    print(i)  # Prints numbers from 0 to 4

# Using a while loop
count = 0
while count < 5:
    print(count)
    count += 1
```
**Note:** `range()` generates a sequence of numbers. `while` loops run until the condition is `False`.

### 5. **Functions**
```python
# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Calling the function
message = greet("Bob")
print(message)
```
**Note:** Functions help organize code into reusable blocks.

### 6. **Lists and Dictionaries**
```python
# List example
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Dictionary example
details = {"name": "John", "age": 30}
print(details["name"])  # Accessing value by key
```
**Note:** Lists store multiple items in an ordered way, while dictionaries store data as key-value pairs.

## 🚀 Keep Practicing!

Python is powerful and beginner-friendly. Keep experimenting with code, and you'll master it in no time. Happy coding! 🐍


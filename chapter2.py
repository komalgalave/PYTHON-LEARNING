# variable s and datatype
# variable is the name given to the memory location in a program
a = 2 
b = 2
# a , b & c is variable or identifier
c = a + b
print(c)

# data type
# 1.integers  2. floating point numbers
# 3. strings  4. booleans  5. none
a = 1 #a is an integer
b = 5.22 #b is an floating point number
c = "harray"#is a string
d = False#d is a boolean variable
e = None#e is a none type variable


# RULES FOR CHOOSING AN IDENTIFIER
# • A variable name can contain alphabets, digits, and underscores.
# • A variable name can only start with an alphabet and underscores.
# • A variable name can’t start with a digit.
# • No while space is allowed to be used inside a variable name.


# OPERATORS IN PYTHON
# Following are some common operators in python:
# 1. Arithmetic operators: +, -, *, / etc.
# 2. Assignment operators: =, +=, -= etc.
# 3. Comparison operators: ==, >, >=, <, != etc.
# 4. Logical operators: and, or, not.

# arithmetic operators
a = 4 - 2
b = 4
c = a + b
print(c)

#  assignment operators
a = 4 - 2
print(a)
b = 6
b += 3#increment the value of bby 3
# b -= 3 decrement the value of b by 3
print(b)

# comparsion (only written boolean)
d = 5<4
print(d)

# logical operators
e = True or False
print(e)

# TYPE() FUNCTION AND TYPECASTING
# type() function is used to find the data type of a given variable in python.
a = 31
c =  type(a) # class <int>
print(c)
# A number can be converted into a string and vice versa (if possible)
# There are many functions to convert one data type into another.
a = "45"
b = int(a)
t = type(b)
print(t)

# INPUT () FUNCTION
# This function allows the user to take input from the keyboard as a string.
# It is important to note that the output of input is always a string (even is a number is entered).

a = int(input("enter number 1 :  "))
b = int(input("enter number 2 :  "))


print("number a is :", a)
print("number b is :", b)
print("sum is:", a + b)



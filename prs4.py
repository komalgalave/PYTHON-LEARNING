# 1. Write a program to store seven fruits in a list entered by the user./
fruit = []
f1 = input("Enter fruit name: ")
fruit.append(f1)
f2 = input("Enter fruit name: ")
fruit.append(f2)
f3 = input("Enter fruit name: ")
fruit.append(f3)
f4 = input("Enter fruit name: ")
fruit.append(f4)
f5 = input("Enter fruit name: ")
fruit.append(f5)
f6 = input("Enter fruit name: ")
fruit.append(f6)
f7 = input("Enter fruit name: ")
fruit.append(f7)
print(fruit)


# 2. Write a program to accept marks of 6 students and display them in a sorted manner.
mark = []
f1 = int(input("Enter mark name: "))
mark.append(f1)
f2 = int(input("Enter mark name: "))
mark.append(f2)
f3 = int(input("Enter mark name: "))
mark.append(f3)
f4 = int(input("Enter mark name: "))
mark.append(f4)
f5 = int(input("Enter mark name: "))
mark.append(f5)
f6 = int(input("Enter mark name: "))
mark.append(f6)
mark.sort()
print(mark)


# 3. Check that a tuple type cannot be changed in python.
# a = (34, 232, "komal")
# a[2] = "tomal"('tuple' object does not support item assignment)



# 4. Write a program to sum a list with 4 numbers.
k = [2, 2, 2, 2]
print(sum(k))


# 5. Write a program to count the number of zeros in the following tuple:
# a = (7, 0, 8, 0, 0, 9)
# Define the tuple
a = (7, 0, 8, 0, 0, 9)

# Count the number of zeros
zero_count = a.count(0)

# Print the result
print("Number of zeros:", zero_count)
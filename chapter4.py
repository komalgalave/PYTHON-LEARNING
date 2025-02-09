# CHAPTER 4 – LISTS AND TUPLES


# Python lists are containers to store a set of values of any data type
friends = ["Apple", "Orange", 5, 345.34, False, "Aakash","komal"]
print(friends[0])
friends[0] = "Grapes"#unlike string lists are mutable
print(friends[0])
print(friends[1:3])


# LIST INDEXING
'''A list can be indexed just like a string.
l1 = [7,9,"harry"]
l1[0] # 7
l1[1] # 9
l1[70] # error
l1[0:2] # [7,9] #list slicing '''


# LIST METHODS
'''Consider the following list:
l1 = [1,8,7,2,21,15]
• l1.sort(): updates the list to [1,2,7,8,15,21]
• l1.reverse(): updates the list to [15,21,2,7,8,1]
• l1.append(8): adds 8 at the end of the list
• l1.insert(3,8): This will add 8 at 3 index
• l1.pop(2): Will delete element at index 2 and return its value.
• l1.remove(21): Will remove 21 from the list. '''
friends = ["Apple", "Orange", 5, 345.34, False, "Aakash","komal"]
print(friends)
friends.append("harry")
print(friends)
l1 = [1, 34, 65, 2, 5, 11]
# l1.sort()
# l1.reverse()
# l1.insert(3, 32224)#insert 32224 such that its index in the list is 3
print(l1.pop(3))
l1.remove(34)
print(l1)


# TUPLES IN PYTHON
'''A tuple is an immutable data type in python
a = () # empty tuple
a = (1,) # tuple with only one element needs a comma
a = (1,7,2) # tuple with more than one element'''
# a = (1, 2, 3, 4, 5)(it is a tuble)
# a = () (empty tuble)
a = (1, )
print(type(a))
# tuble is immutable


# TUPLE METHODS
a = (1, 45, 34, 23, 234, "rohan", "komal")
print(a)
no = a.count(45)
print(no)



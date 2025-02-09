# CHAPTER 5 – DICTIONARY & SETS
# Dictionary is a collection of keys-value pairs.
marks = {
    "komal": 100,
    "rohan": 100,
    "keshav": 100
}
print(marks, type(marks))
print(marks["komal"])


'''PROPERTIES OF PYTHON DICTIONARIES
1. It is unordered.
2. It is mutable.
3. It is indexed.
4. Cannot contain duplicate keys.'''


# DICTIONARY METHODS
marks = {
    "komal": 100,
    "rohan": 100,
    "keshav": 100
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"komal": 110})
print(marks)
print(marks.get("komal"))

# • a.items(): Returns a list of (key,value)tuples.
# • a.keys(): Returns a list containing dictionary's keys.
# • a.update({"friends":}): Updates the dictionary with supplied key-value pairs.
# • a.get("name"): Returns the value of the specified keys (and value is returned
# eg."harry" is returned here)


# SETS IN PYTHON.
# Set is a collection of non-repetitive elements.
# PROPERTIES OF SETS
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.


s = {1, 5, 32, 3, 3 , 2 , 4, 5}
e = set()#dont use s = {}as it will create an empty dictionary
print(s,type(s))
s.add(566)
print(s, type(s))


'''# OPERATIONS ON SETS
Consider the following set:
s = {1,8,2,3}
• len(s): Returns 4, the length of the set
• s.remove(8): Updates the set s and removes 8 from s.
• s.pop(): Removes an arbitrary element from the set and return the element
removed.
• s.clear():empties the set s.
• s.union({8,11}): Returns a new set with all items from both sets. {1,8,2,3,11}.
• s.intersection({8,11}): Return a set which contains only item in both sets {8}.'''


s = {1, 5, 32, 3, 3 , 2 , 4, 5}
e = set()#dont use s = {}as it will create an empty dictionary
print(s,type(s))
s.add(566)
print(s, type(s))
s.remove(1)
print(s)
len(s)
print(s)

# union amd intersection
s1 = {1, 2, 3, 4, 5}
s2 = {9, 8, 21, 4, 5}
print(s1.union(s2))
print(s1.intersection(s2))

# CHAPTER 3 – STRINGS


# String is a data type in python.
# String is a sequence of characters enclosed in quotes.
# We can primarily write a string in these three ways.
a ='harry' # Single quoted string
b = "harry" # Double quoted string
c = '''harry''' # Triple quoted string

a = "komal"
print(a)

# STRING SLICING (it is inmutable)
# A string in python can be sliced for getting a part of the strings.
name = "komal"
nameshort = name[0:3]#start from index 0 all the way till 3(excluding 3)
print(nameshort)
character1 = name[3]
print(character1)


#  Indices
name = "Komal"
print(name[0:3])
print(name[-4: -1])#negative indices
print(name[1:4])
print(name[:3])
print(name[0:])


# SLICING WITH SKIP VALUE
# We can provide a skip value as a part of our slice like this:
name = "12345678910"
print(name[1:3:2])


'''STRING FUNCTIONS
# Some of the commonly used functions to perform operations on or manipulate strings are as follows. Let us assume there is a string ‘str’ as follows:
# str = 'harry' (Now when operated on this string ‘str’, these functions do the following:)

# 1. len () function – This function returns the length of the strings.
 str = "harry"
 print(len(str)) # Output: 5

# 2. String.endswith("rry") – This function_ tells whether the variable string ends with the string "rry" or not. 
 If string is "harry", it returns true for "rry" since Harry ends with rry.
 str = "harry"
 print(str.endswith("rry")) # Output: True

# 3. string.count("c") – counts the total number of occurrences of any character.
 str = "harry"
 count = str.count("r")
 print(count) # Output: 2

# 4. the first character of a given string.
 str = "harry"
 capitalized_string = str.capitalize()
 print(capitalized_string) # Output: "Harry"

# 5. string.find(word) – This function friends a word and returns the index of first
 occurrence of that word in the string.
 str = "harry
 index = str.find("rr")
 print(index) # Output: 2

# 6. string.replace (old word, new word ) – This function replace the old word with
new word in the entire string.
str = "harry"
replaced_string = str.replace("r", "l")
print(replaced_string) # Output: "hally"'''

name = "komal"
print(len(name))
print(name.endswith("rry"))
print(name.startswith("ko"))
print(name.capitalize())



# ESCAPE SEQUENCE CHARACTERS
'''Sequence of characters after backslash "\" → Escape Sequence characters
Escape Sequence characters comprise of more than one character but represent one
character when used within the strings'''

a = "\tkomal if you want to become \n successfull then you need to study. \n \"regularly\""
print(a)

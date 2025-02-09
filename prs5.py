# 1. Write a program to create a dictionary of Hindi words with values as their English
#     translation. Provide user with an option to look it up!
words = {
    "namsate": "Hello",
    "tk": "Thank you",
    "pustak": "Book",
    "ghar": "House",
}
word = input("Enter the word you want meanning of : ")
print(words[word])

# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).
s = set()
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
print(s)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it
s = set()
s.add(18)
s.add("18")
print(s)

# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s)
print(len(s))

# 5. s = {} What is the type of 's'?
s = {}
print(type(s))

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
d = {}

name = input("Enter frinds name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter frinds name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter frinds name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter frinds name: ")
lang = input("Enter language name: ")
d.update({name: lang})

print(d)

# 7. If the names of 2 friends are same; what will happen to the program in problem6?
# the value enter later will be update


# 8. If languages of two friends are same; what will happen to the program in problem6?
# nothing will happen the value can be same


# 9. Can you change the values inside a list which is contained in set S? s = {8, 7, 12, "Harry", [1,2]}
# no, you cannot add a list to a set because lists are mutable and sets only allow immutable elements. If needed, use a tuple instead:
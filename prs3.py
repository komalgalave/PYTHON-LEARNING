# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.
name = input("Enter your name: ")
print(f"good morning, {name} ")

# 2. Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","komal").replace("<|Date|>","28 april 2025"))


# 3. Write a program to detect double space in a string.
name = "komal is good  girl"
print(name.find("  "))#give index value


# 4. Replace the double space from problem 3 with single spaces.
name = "komal is good  girl"
print(name.replace("  "," "))
print(name)#string is immutable which cannot change them by running function on them


# 5. Write a program to format the following letter using escape sequence characters.
letter = "Dear Harry, \n\tthis python course is nice.\n Thanks!"
print(letter)
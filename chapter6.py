# CHAPTER 6 – CONDITIONAL EXPRESSION
'''Sometimes we want to play PUBG on our phone if the day is Sunday.
Sometimes we order Ice Cream online if the day is sunny.
Sometimes we go hiking if our parents allow.
All these are decisions which depend on a condition being met.
In python programming too, we must be able to execute instructions on a condition(s)
being met.
This is what conditionals are for!'''

# IF ELSE AND ELIF IN PYTHON
'''If else and elif statements are a multiway decision taken by our program due to certain
conditions in our code.'''

# If else statement

a = int(input("Enter your age: "))

if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

else:
    print("You are below the age of consent")

print("End of program")


# IF ELIF ELSE LADDER

b = int(input("Enter Your age: "))

if(b>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(b<0):
    print("Your are entering invalid negative age")

elif(b==0):
       print("You are entering 0 which is not a valid age")
      

else:
    print("You are below the age of consent")


print("End of program")


#  Write a program to print yes when the age entered by the user is greater than or equal to 18.
c = int(input("Enter your age: "))

if(c>=18):
     print("yes")

else:
     print("Your are not 18")

print("stop")


# RELATIONAL OPERATORS(similar to comporator operator)
'''Relational Operators are used to evaluate conditions inside the if statements. Some
examples of relational operators are:
==: equals.
> =: greater than/ equal to.
< =: lesser than/ equal to.
'''

# LOGICAL OPERATORS/
'''In python logical operators operate on conditional statements. For Example:
• and – true if both operands are true else false.
• or – true if at least one operand is true or else false.
• not – inverts true to false & false to true'''

# ELIF CLAUSE
'''elif in python means [else if]. An if statements can be chained together with a lot of
these elif statements followed by an else statement.
'''
# multiple if statement
m = int(input("Enter Your age: "))

# if statement no: 1
if(a%2 == 0):
     print("m is even ")

# if statement no: 2

if(m>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(m<0):
    print("Your are entering invalid negative age")

elif(m==0):
       print("You are entering 0 which is not a valid age")
      

else:
    print("You are below the age of consent")


print("End of program")
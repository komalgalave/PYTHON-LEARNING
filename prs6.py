# 1. Write a program to find the greatest of four numbers entered by the user
a1 = int(input("Enter the number 1: "))
a2 = int(input("Enter the number 2: "))
a3 = int(input("Enter the number 3: "))
a4 = int(input("Enter the number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1:" ,a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2:" ,a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a3:" ,a3)

elif(a4>a1 and a4>a3 and a4>a2):
    print("Greatest number is a4:" ,a4) 



#  2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

marks1 = int(input("Enter mark 1:"))
marks2 = int(input("Enter mark 2:"))
marks3 = int(input("Enter mark 3:"))

# check for total percentage
total_percentage = (100*(marks1 + marks2 +marks3))/300
if(total_percentage>=40 and  marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed:" , total_percentage)
else:
    print("You failed , try again next year:", total_percentage)


# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4= "click this"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")




# 4. Write a program to find whether a given username contains less than 10
# characters or not.
username = input("Enter username: ")

if(len(username)<10):
    print("Your username contains less then 10 characters")

else:
    print("All is well!")

# 5. Write a program which finds out whether a given name is present in a list or not.

l = ["Komal" , "Shivam" , "Divya" , "Insta"]

name = input("Enter your name : ")

if(name in l):
    print("Your name is in the list")

else:
    print("Your name is not in the list")



# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

markss = int(input("Enter your markss: "))

if(markss<=100 and markss>=90):
    grade = "Ex"
elif(markss<=90 and markss>=80):
    grade = "A"
elif(markss<80 and markss>=70):
    grade = "B"
elif(markss<70 and markss>=60):
    grade = "C"
elif(markss<60 and markss>=50):
    grade = "D"
elif(markss<=50):
    grade = "f"

print("Your gade is:", grade)



# 7. Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter the post: ")

if("harry" in post.lower()):
    print("This post is talkong about harry")

else:
    print("This post is not talkong about harry")
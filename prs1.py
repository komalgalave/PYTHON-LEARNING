# problem 1
# write a program to print twinkle twinkle litte star poem in python
print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.''')



# use REPL and print the table of 5 usnig it(use terminal)

# install an external module and use it to perform an operation of your interest
import pyttsx3
engine = pyttsx3.init()
engine.say("thanks to creating me i am very great full plases tell that you want to know and tell how whase your life going and also assinge me my day to day responsiblility okay what are you doing where and i am ia creating by i meta  ")
engine.runAndWait()


# write a python program to print the contents of a directory using OS module search online for the function which does that
import os

directory = '/'

contents = os.listdir(directory)

for item in contents:
    print(item)


# lavel the program written in python 4 with comment

import os

directory = '/'# specify the directory you want to list

contents = os.listdir(directory)# get the list of files and directories

for item in contents:
    print(item)# print the contents



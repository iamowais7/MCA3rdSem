'''    Write a program to pick a random character from a given String supplied by 
       the user.  '''


import random

user_string= input("Enter the string :\n")

if len(user_string) > 0:
    random_char = random.choice(user_string)
    print(f"Random character selected is : {random_char}")
else:
    print("Input string is empty ")    
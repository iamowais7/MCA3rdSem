''' Write a program to generate a random Password which meets the following 
conditions 
a. Password length must be 10 characters long. 
b. It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.'''


import random
import string

def generated_password():
    upper_case = random.choices(string.ascii_uppercase,k=2)
    digit = random.choice(string.digits)
    special_symbol = random.choice(string.punctuation)
    other_char = random.choices(string.ascii_letters + string.digits + string.punctuation , k=6)
      
    #here we are merging string and list thats why we have used [] brackets
    password_list = upper_case + [digit] + [special_symbol] + other_char
    
    random.shuffle(password_list)
    # converting list into string
    password = ''.join(password_list)
    return password

password = generated_password()
print(f"Generated password will be :{password}")
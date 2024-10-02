'''Write a program to accept a string and display: 
   a. Number of uppercase characters 
   b. Number of lowercase characters 
   c. Total number of alphabets 
   d. Number of digits '''
 
import string   
string = input("Enter the string : ")

uppercase_count = 0
lowercase_count = 0
alpha_count = 0
digit_count = 0

for i in string:
   if i.isupper():
      uppercase_count += 1
   if i.islower():
      lowercase_count += 1
   if i.isalpha():
      alpha_count += 1 
   if i.isdigit():
      digit_count += 1
print(f"Number of uppercase char are {uppercase_count}")
print(f"Number of lowercase char are {lowercase_count}")           
print(f"Total number of alphabets present are {alpha_count}")           
print(f"Number of digits present are {digit_count}")           
           
         
      
       







   
   
   
   
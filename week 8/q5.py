'''Write a python program that reads a string which contains English alphabets and 
   numbers. The program should create two lists L1 and L2, where L1 includes all the 
   numbers present in the string while L2 includes all the alphabets of the string. '''
   
   
import string

s = str(input("Enter the string : "))
list_1 = []
list_2 = []

for i in s:
    if i.isalpha():
        list_1.append(i)
    
    if i.isdigit():
        list_2.append(i)     
   
   
print("Alphabets list are : ",list_1)
print("Numbers list are : ",list_2)   
   
   
   
   
   
   
   
   
   
   
   
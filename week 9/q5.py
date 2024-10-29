'''Write a program in python to find alphabet/s having maximum number of instances 
   in a given file. '''

from collections import Counter

with open (r"D:\CAMS-3P01\week 9\file.txt","r") as file :
   file_lines = file.read().lower()
   count =0
   alphabetic_char = [char for char in file_lines if char.isalpha()]
   
   alphabet_count = Counter(alphabetic_char)
   
   max_occurence = max(alphabet_count.values())
   
   max_occurred_alphabets = [char for char, count in alphabet_count.items() if count == max_occurence]
   
   print(f"Max occured char in file is : {max_occurred_alphabets}")

   







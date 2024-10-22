'''Write a program in python to find vowels having maximum number of instances in a 
   given file. 
   (Note: File contains variety of data such as English alphabets, numbers etc.). '''
   
   

vowels = 'aeiouAEIOU'

vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

with open(r"D:\CAMS-3P01\week 8\file.txt", "r") as f:
    for line in f:
        for char in line:
            if char.lower() in vowel_count:
                vowel_count[char.lower()] += 1


max_vowel = max(vowel_count, key=vowel_count.get)
max_count = vowel_count[max_vowel]


print(f"The vowel '{max_vowel}' appears the most with {max_count} occurrences.")

   
   
   
   
   
   
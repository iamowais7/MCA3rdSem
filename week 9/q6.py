'''A file contains information about programs and courses in the following format: 
   Program,course. Write a Python program to find the number of courses against each 
   program. 
   Eg: 
   Program,Course 
   MCA,Database 
   MCA,Java 
   M.Sc,Data Structure 
   B.Sc, Python '''
   
   
with open(r"D:\CAMS-3P01\week 9\file1.txt","r") as file:
    program_courses ={}
    file.readline()
    for line in file:
         line = line.strip()  
         if line:  
            program, course = line.split(',') 
        
            if program in program_courses:
               program_courses[program] += 1
            else :
               program_courses[program] = 1
        
    for program , count in  program_courses.items():
           print(f"{program} : {count} courses ")
   
   
   
   
 
 
 
 
 
   
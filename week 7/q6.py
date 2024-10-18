'''Consider two files having some lines of statements. Write a Python program to swap 
   content present at middle line of first file with the content of last line of the second 
   file. (Note: First file contains odd numbers of lines of statement) '''
   
   
def swap_content(file1,file2):
    with open (file1,'r') as f1:
        lines_file1 = f1.readlines()
        
    with open (file2,'r') as f2:
        lines_file2 = f2.readlines()
        
    middle_index_file1 = len(lines_file1)//2
    
    last_index_file2 = len(lines_file2) - 1
    
    #swapping content of file1 with file2
    lines_file1[middle_index_file1], lines_file2[last_index_file2] = lines_file2[middle_index_file1] , lines_file1[last_index_file2]
   
    with open(file1,'w') as f1:
        f1.writelines(lines_file1)
    
    with open(file2,'w') as f2:
        f2.writelines(lines_file2)
            
    print(f"Middle line of {file1} swapped with last line of {file2}.")
            
file_1 = r'D:\CAMS-3P01\week 7\file1.txt'
file_2 = r'D:\CAMS-3P01\week 7\file2.txt'

swap_content(file_1,file_2)
      
   
   
   
   
   
   
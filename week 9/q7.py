'''A file contains information about employees with the following parameters: Name, 
   Id, Salary, Dname. Write a Python program to write one more column HRA (House 
   rent allowances) to this file, where HRA= 18%of salary 
   Eg: Suppose the existing file is as follows, where you need to add HRA column: 
   Name,id,salary, Dname 
   Amar,101,20000,Sales 
   Ammar,102,22000,Marketing 
   Rahil,103,18000,Sales '''

import csv

with open(r"D:\CAMS-3P01\week 9\employees.csv", "r") as file :
    reader = csv.reader(file)  #(it will treat as rows in file)
    lines = list(reader)

#adding hra column
header = lines[0] + ['HRA']
updated_lines = [header]

for line in lines[1:]:
    name, emp_id, salary, dname = line[0], line[1], float(line[2]), line[3]
    hra = salary* 0.18
    updated_line = [name, emp_id, salary, dname, hra]
    updated_lines.append(updated_line)

with open(r"D:\CAMS-3P01\week 9\employees.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(updated_lines)

print("HRA added to employee file successfully.")














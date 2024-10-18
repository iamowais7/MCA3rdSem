'''Consider two files that contain information about Employees and Departments in the 
   following parameters: Employee (Name, EId, Salary, DID), Department (DID, 
   DName, DLocation). Write a Python program to find the average salary of each 
   department.'''
 
import csv
from collections import defaultdict


def calculate_average_salary(employee_file, department_file):
    
    employee_data = []
    with open(employee_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employee_data.append({
                'Name': row['Name'],
                'EId': row['EId'],
                'Salary': float(row['Salary']),
                'DID': row['DID']
            })
    
    
    department_data = {}
    with open(department_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            department_data[row['DID']] = {
                'DName': row['DName'],
                'DLocation': row['DLocation']
            }
    
    
    salary_by_department = defaultdict(list)
    for employee in employee_data:
        salary_by_department[employee['DID']].append(employee['Salary'])
    
   
    for did, salaries in salary_by_department.items():
        avg_salary = sum(salaries) / len(salaries)
        department = department_data[did]
        print(f"Department: {department['DName']}, Location: {department['DLocation']}, "
              f"Average Salary: {avg_salary:.2f}")
        

employee_file = 'D:\CAMS-3P01\week 7\employees.csv'  
department_file = 'D:\CAMS-3P01\week 7\departments.csv'  


calculate_average_salary(employee_file, department_file)
   
   
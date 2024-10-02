'''Write a program to get roll numbers, names, and marks of students and store these 
   details in a file called "Marks. data".'''
   

def store_student_details():
    
    with open("Marks.data", "w") as file:
        num_students = int(input("Enter the number of students: "))
        
        for _ in range(num_students):
            
            roll_number = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            marks = input("Enter Marks: ")
            
           
            file.write(f"Roll Number: {roll_number}, Name: {name}, Marks: {marks}\n")
    
    print("Student details have been stored in 'Marks.data'.")


if __name__ == "__main__":
    store_student_details()
   
   
   
   
   
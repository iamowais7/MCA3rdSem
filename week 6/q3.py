''' Write a Python program to calculate the sum of squares of the first two digits and the 
    last two digits of a 4-digit number, e.g., for 1233, calculate 12^2 + 33^2.'''
    
    
num = input("Enter the number : ")

if len(num) != 4:
    print("Enter a valid number having 4 digits ")   
else:
    number = int(num)
    last_digits = number % 100
    number = number // 100 
    answer = number*number + last_digits*last_digits
    print(answer)

  

     
        
    
    
    
    
    
    
    
    
    
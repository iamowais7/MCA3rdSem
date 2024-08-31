
def fact(num):
    result = 1
    for i in range(2, num + 1):
        result *= i  
    return result


num = int(input("Enter the number: "))
factorial = fact(num)
print(f"The factorial of {num} is: {factorial}")

def sum_of_digits(num):
    num = abs(num)  
    total_sum = 0
    while num > 0:
        digit = num % 10  
        total_sum += digit  
        num = num // 10  
    return total_sum


num = int(input("Enter an integer: "))
sum_digits = sum_of_digits(num)
print(f"The sum of the digits of {num} is: {sum_digits}")
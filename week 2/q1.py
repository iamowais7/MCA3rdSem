num = int(input("Enter the number\n"))
print("Reverse order will be")
while(num > 0):
    digit = num % 10 
    print(digit,end='')
    num = num // 10
print(" ")
   
def func(lst):
    if lst[0] == lst[-1]:  
        return True
    return False

user_input = input("Enter the elements separated by spaces: \n")
lst = user_input.split() 



print(func(lst))  

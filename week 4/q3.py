user_input = input("Enter the elements separated by spaces: \n")
lst = user_input.split() 
my_lst = [int(i) for i in lst]
for i in my_lst:
    i = i*i
    print(i)


 

'''Write a Python program to create a list of user’s supplied distinct integers having 
   even number of elements. The program further creates two lists of equal lengths 
   based on the original list, where first list is having all elements less than elements of 
   second list. Display both the lists. '''


def create_original_list():
    original_list = []
    while True:
        try:
            n = int(input("Enter the number of distinct integers (must be even): "))
            if n % 2 != 0:
                print("The number of elements must be even. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while len(original_list) < n:
        try:
            element = int(input(f"Enter distinct integer {len(original_list) + 1}: "))
            if element not in original_list:
                original_list.append(element)
            else:
                print("Duplicate value entered. Enter a distinct integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    return original_list


def split_list(original_list):
    
    sorted_list = sorted(original_list)
    
    
    half_size = len(sorted_list) // 2
    list_1 = sorted_list[:half_size]  
    list_2 = sorted_list[half_size:]  
    
    return list_1, list_2


original_list = create_original_list()


list_1, list_2 = split_list(original_list)


print("List 1 (smaller elements):", list_1)
print("List 2 (larger elements):", list_2)







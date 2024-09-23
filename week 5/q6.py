'''Write a program create a numpy array and sort as per below cases: 
   a. Case 1: Sort array by the second row. 
   b. Case 2: Sort the array by the second column.'''
   
import numpy as np

# Function to sort by the second row
def sort_by_second_row(arr):
    # Sorting by the second row (index 1)
    return arr[:, arr[1, :].argsort()]

# Function to sort by the second column
def sort_by_second_column(arr):
    # Sorting by the second column (index 1)
    return arr[arr[:, 1].argsort()]


array = np.array([[34, 23, 12, 45, 56],
                  [14, 53, 25, 67, 19],
                  [67, 89, 45, 23, 12]])

print("Original Array:")
print(array)

# Case 1: Sort by the second row
sorted_by_second_row = sort_by_second_row(array)
print("\nArray sorted by the second row:")
print(sorted_by_second_row)

# Case 2: Sort by the second column
sorted_by_second_column = sort_by_second_column(array)
print("\nArray sorted by the second column:")
print(sorted_by_second_column)
   
   
   
   
   
   
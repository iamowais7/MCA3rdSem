''' Write a program to create a numpy array and return array of odd rows and even 
    columns from the numpy array. '''
    
import numpy as np

# Function to return odd rows and even columns from the numpy array
def odd_rows_even_columns(arr):
    # Odd rows correspond to 1st, 3rd, 5th, etc. (index 0, 2, 4, ...)
    # Even columns correspond to 2nd, 4th, 6th, etc. (index 1, 3, 5, ...)
    return arr[::2, 1::2]

# Example array creation
array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]])

# Get the odd rows and even columns
result = odd_rows_even_columns(array)

# Display the result
print("Original Array:")
print(array)
print("\nArray with Odd Rows and Even Columns:")
print(result)

    
    
    
    
    
    
    
    
    
    
    
    
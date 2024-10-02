'''Write a Python program that inputs two tuples and creates a third that contains all 
   elements of the first followed by all elements of the second. '''


tuple1 = tuple(input("Enter elements of the first tuple, separated by space: ").split())
tuple2 = tuple(input("Enter elements of the second tuple, separated by space: ").split())


tuple3 = tuple1 + tuple2


print("The combined tuple is:", tuple3)








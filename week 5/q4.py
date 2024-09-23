'''Given a two list of numbers, write a program to create a new list such that the 
   new list should contain odd numbers from the first list and even numbers from 
   the second list.'''
   
list1 = []
list2 = []

n = int(input("Enter the value of n for list1 :"))

for i in range(n):
   element = int(input(f"Enter the {i+1} element :"))
   list1.append(element)
   
m = int(input("Enter the value of m for list2 :"))
   
for j in range(m):
   element = int(input(f"Enter the {i+1} element :"))
   list2.append(element)   
    

def create_list(list1 , list2):
   list3 = []
   
   for i in list1:
       if i%2 != 0:
          list3.append(i)
   
   for j in list2:
       if j%2 ==0:
          list3.append(j)
   
   return list3      

list3 = create_list(list1,list2)
print(list3)         
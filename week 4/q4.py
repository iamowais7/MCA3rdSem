list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']


for i in range(len(list1)):
    print(f"List 1: {list1[i]}, List 2: {list2[-(i+1)]}")
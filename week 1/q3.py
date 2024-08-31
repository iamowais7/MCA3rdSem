list = []
for i in range(20):
     element = int(input("Enter the respective numbers\n"))
     list.append(element)
for x in range(0 ,20):
        temp = list[x]
        if (temp % 5 == 0):
          print(temp)
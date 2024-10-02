'''Write a Python program to create a dictionary with names and phone numbers. Then 
   ask the user for a name and print the corresponding phone number. '''


phone_number_record = {
   'owais':'7055786791',
   'altamash':'7078567820',
   'faiz' : '7017107783',
   'hammad' : '9897123309'
}

name = input("enter the name :")

if name in phone_number_record:
   print(f"Corresponding phone number : {phone_number_record[name]}") 
else:
   print("No such record exist ..")



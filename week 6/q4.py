'''Write a program that inputs a main string and creates an encrypted string by 
   embedding a short symbol-based string after each character. The program should 
   also decrypt the string. '''
   
# Function to encrypt the string
def encrypt(main_string, symbol_string):
    encrypted_string = ""
    for char in main_string:
        encrypted_string += char + symbol_string
    return encrypted_string

# Function to decrypt the string
def decrypt(encrypted_string, symbol_string):
    symbol_length = len(symbol_string)
    decrypted_string = ""
    i = 0
    while i < len(encrypted_string):
        decrypted_string += encrypted_string[i]
        i += symbol_length + 1
    return decrypted_string


if __name__ == "__main__":
    
    main_string = input("Enter the main string to be encrypted: ")
    symbol_string = input("Enter the symbol-based string: ")

    
    encrypted_string = encrypt(main_string, symbol_string)
    print(f"Encrypted string: {encrypted_string}")

    
    decrypted_string = decrypt(encrypted_string, symbol_string)
    print(f"Decrypted string: {decrypted_string}")
   
   
   
   
   
   
   
   
   
   
   
   
   
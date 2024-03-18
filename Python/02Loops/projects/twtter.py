#Get user input
user_input = input("Input: ")
#List all the vowels, these will need to be removed
vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]



# Replace vowels when printed
modified_input = ""
for char in user_input:
    if char not in vowels:
        modified_input += char

print(modified_input)
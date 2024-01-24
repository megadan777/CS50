#SUBMITTED TO CS50
# Creating an input from the user
message = input("Enter some text: ")

# replacing each space with ... (i.e., three periods).
message = message.replace(' ', '...')

print(f"{message}")
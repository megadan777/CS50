# Creating an input from the user
def(main):
message = input("Enter some text: ")

# replacing each space with ... (i.e., three periods).
message = message.replace(' ', '...')

print(f"{message}")


main()
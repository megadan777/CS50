#SUBMITTED TO CS50
# Creating an input from the user
lowercase = input("Enter some text: ")

# Remove whitespace from the str and make all text lowercase
lowercase = lowercase.strip().lower()

print(f"{lowercase}")
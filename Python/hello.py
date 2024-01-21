# Ask user for their name
name = input ("What's your name? ")

#Remove whitespace from str and capitlise user name
name = name.strip().title()

#Format Strings
print(f"hello, {name}")
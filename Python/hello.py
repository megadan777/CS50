# Ask user for their mnname
name = input ("What's your name? ")

#Remove whitespace from str and capitlise user name
name = name.strip()

#Capitilise user name
name = name.title()

#Format Strings
print(f"hello, {name}")
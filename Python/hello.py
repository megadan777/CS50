# Ask user for their name and Remove whitespace from str and capitlise user name
name = input ("What's your name? ").strip().title()

#Split name into first and last
first, last  name.split(" ")

#Format Strings
print(f"hello, {first}")
deep = input("What is the Great Question of Life, the Universe and Everything? ").strip()

if deep == "42" or deep == "forty-two" or deep == "Forty Two":
    print("Yes")
elif deep.title() == "Forty Two":
    print("Yes")
elif deep.lower() == "forty-two":
    print("Yes")
else:
    print("No")

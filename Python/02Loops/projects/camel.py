variable = input("camelCase: ")

def main():
    word = ""
    # Iterate over alphabet in variable

    for alphabet in variable:
        if alphabet.isupper():
            word += "".join("_" + alphabet.lower())
        else:
            word += "".join(alphabet)

    print(word)

main()
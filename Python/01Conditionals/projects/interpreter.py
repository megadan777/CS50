def main():
    interpret = input("Enter your arithmetic expression: ")
    convert(interpret)

def convert(s):
    x, y, z = s.split(" ")

    x = float(x)
    z = float(z)

    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "*":
        print(x * z)
    elif y == "/":
        print(x / z)

main()
greeting = input("Input a greeting: ").strip().lower()

if greeting.lower() == "hello" or greeting.lower() == "hello there" or greeting.lower() == "hello, newman":
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")

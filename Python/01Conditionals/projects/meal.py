def main():
    time = input("What time is it? ").strip()
    converted_time = convert(time)
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")
    else:
        print("")

def convert(time):
    x, y = map(int, time.split(":"))
    converted_time = x + y/60
    return converted_time

if __name__ == "__main__":
    main()

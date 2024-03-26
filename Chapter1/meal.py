def main():
    time = input("What time is it? ").strip().split(":")
    meal = convert(time)
    if not meal:
        print("Invalid Input")
    else:
        print(meal)


def convert(time):
    hour, minute = time
    if len(time) == 2:
        try:
            time = int(hour) + int(minute) / 60
        except:
            return False
        if 7 <= time <= 8:
            return "breakfast time"
        elif 12 <= time <= 13:
            return "lunch time"
        elif 18 <= time <= 19:
            return "dinner time"
        else:
            return "It's not time to eat yet!"
    else:
        return False


if __name__ == "__main__":
    main()

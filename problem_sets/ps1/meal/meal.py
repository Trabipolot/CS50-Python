def main():
    time = input("What time is it? ").strip()
    time_float = convert(time)
    if not time_float:
        print("Invalid Input")
    else:
        print(meal_time(time_float))


def convert(time: str):
    hour_minute = time.split(":")
    if len(hour_minute) == 2:
        try:
            time_float = int(hour_minute[0]) + int(hour_minute[1]) / 60
            return time_float
        except:
            return False
    else:
        return False


def meal_time(time: float) -> str:
    if 7 <= time <= 8:
        return "breakfast time"
    elif 12 <= time <= 13:
        return "lunch time"
    elif 18 <= time <= 19:
        return "dinner time"
    else:
        return "It's not time to eat yet!"


if __name__ == "__main__":
    main()

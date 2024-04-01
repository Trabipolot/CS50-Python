def main():
    while True:
        fraction: str = input("Enter a fraction: ").strip()
        percentage: int = convert(fraction)
        if percentage is not None:
            break
    output = gauge(percentage)
    print(output)


def convert(fraction: str) -> int:
    percentage = None  
    try:
        x, y = fraction.split("/")
        percentage = int(x) / int(y) * 100
    except Exception as e:
        print(e)
        return None
    if percentage is not None:
        if percentage <= 100:
            return round(percentage)
        else:
            print("Invalid Fraction. Value must be between 0 and 1.")
            return None


def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

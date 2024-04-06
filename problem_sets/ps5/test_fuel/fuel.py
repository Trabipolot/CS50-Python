def main():
    percentage = None
    while True:
        fraction: str = input("Enter a fraction: ").strip()
        percentage = convert(fraction)
        if percentage is not None:
            break
    output = gauge(percentage)
    print(output)


def convert(fraction: str):
    percentage = None
    x, y = fraction.split("/")
    percentage = int(x) / int(y) * 100
    if percentage is not None:
        if percentage <= 100:
            return round(percentage)
        else:
            raise ValueError


def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

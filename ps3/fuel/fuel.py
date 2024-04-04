def main():
    percentage = convert_fraction()
    output = create_output(percentage)
    print(output)


def convert_fraction():
    while True:
        percentage = None
        fraction = input("Enter a fraction: ").strip()
        try:
            x, y = fraction.split("/")
            percentage = int(x) / int(y) * 100
        except Exception as e:
            print(e)
        if percentage is not None:
            if percentage <= 100:
                return percentage
            else:
                print("Invalid Fraction. Value must be between 0 and 1.")


def create_output(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

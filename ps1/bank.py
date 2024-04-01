def main():
    greeting = input("Enter a greeting: ").strip().lower()
    payout = check_greeting(greeting)
    print(payout)


def check_greeting(greeting):
    if greeting.startswith("hello"):
        return "0$"
    elif greeting.startswith("h"):
        return "20$"
    else:
        return "100$"


if __name__ == "__main__":
    main()

import json
import requests
import sys


def main():
    n: float = get_command_line_argument()
    rate: float = get_rate()
    price: float = calculate_price(n, rate)
    print(f"${price}")


def get_command_line_argument() -> float:
    arguments: list["str"] = sys.argv
    if len(arguments) <= 2:
        try:
            n: float = float(arguments[1].strip())
            return n
        except ValueError:
            sys.exit("Invalid or missing command-line argument")
    else:
        sys.exit("Too many command-line arguments given")


def get_rate() -> float:
    try:
        response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json"
        ).json()
    except (requests.RequestException, json.JSONDecodeError) as e:
        print(f"The following Error occured, while getting response form URL: {e}")
        sys.exit()
    rate: float = response["bpi"]["USD"]["rate_float"]
    return rate


def calculate_price(amount: float, rate: float) -> float:
    price = format(amount * rate, ",.4f")
    return price


if __name__ == "__main__":
    main()

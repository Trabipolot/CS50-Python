import sys
from tabulate import tabulate
import csv


def extract_data(file) -> list:
    menu: list = []
    reader = csv.DictReader(file)
    for row in reader:
        menu.append(row)
    return menu

def check_input(user_input: list[str], filetype: str, number_of_arguments: int = 1) -> str:
    if len(user_input) == number_of_arguments + 1:
        if user_input[1].endswith(filetype):
            return user_input[1]
        else:
            print(f"Argument does not end with {filetype}")
    elif len(user_input) < number_of_arguments + 1:
        print("Too few command-line arguments")
    else:
        print("Too many command-line arguments)")
    sys.exit()


def read_file(filename: str) -> list[str]:
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()


def main():
    file_path: str = check_input(sys.argv, ".csv")
    file = read_file(file_path)
    menu = extract_data(file)
    print(tabulate(menu, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()

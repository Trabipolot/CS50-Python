import sys
from tabulate import tabulate
import csv
from lines import check_input, read_file


def extract_data(file) -> list:
    menu: list = []
    reader = csv.DictReader(file)
    for row in reader:
        menu.append(row)
    return menu


def main():
    file_path: str = check_input(sys.argv, ".csv")
    file = read_file(file_path)
    menu = extract_data(file)
    print(tabulate(menu, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()

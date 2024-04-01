import sys
import csv


def check_input(
    user_input: list[str], filetype: str, number_of_arguments: int = 1
) -> str:
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
    student = []
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()


def extract_data(file: list[str]) -> list[dict]:
    students = []
    for student in file[1:]:
        try:
            last, first, house = student.replace('"', "").split(",")
            students.append(
                {"first": first.strip(), "last": last.strip(), "house": house.strip()}
            )
        except Exception as e:
            print(e)
    return students


def save_data(data, filename):
    with open(f"{filename}.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, ["first", "last", "house"])
        writer.writeheader()
        writer.writerows(data)


def main():
    file_path = check_input(sys.argv, ".csv", 2)
    file = read_file(file_path)
    students = extract_data(file)
    save_data(students, sys.argv[2])


if __name__ == "__main__":
    main()

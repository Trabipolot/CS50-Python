import sys


def check_input(
    user_input: list[str], filetype: str, number_of_arguments: int = 1
) -> str:
    if len(user_input) == number_of_arguments + 1:
        if user_input[1].endswith(filetype):
            return user_input[1]
        else:
            sys.exit(f"Argument does not end with {filetype}")
    elif len(user_input) < number_of_arguments + 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments)")


def read_file(filename: str) -> list[str]:
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")


def count_lines(file: list[str]) -> int:
    lines = 0
    for row in file:
        if not row.strip().startswith("#") and not row.isspace():
            lines += 1
    return lines


def main():
    file_path: str = check_input(sys.argv, ".py", 1)
    file: list[str] = read_file(file_path)
    lines: int = count_lines(file)
    print(lines)


if __name__ == "__main__":
    main()

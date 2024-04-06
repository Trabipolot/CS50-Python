import PIL
import sys


def check_input(
    user_input: list[str], filetype: str, number_of_arguments: int = 1
) -> str:
    if len(user_input) == number_of_arguments + 1:
        if user_input[1].lower().endswith(filetype):
            return user_input[1]
        else:
            print(f"Argument does not end with {filetype}")
    elif len(user_input) < number_of_arguments + 1:
        print("Too few command-line arguments")
    else:
        print("Too many command-line arguments)")
    sys.exit()


def main():

    filename = check_input(sys.argv, (".jpeg", ".jpg", ".png"), 1)


if __name__ == "__main__":
    main()

def main():
    camel_case = input("Please enter variable name: ")
    snake_case = convert_to_snake_case(camel_case)
    print(f"Camel Case: {camel_case}\nSnake Case: {snake_case}")


def convert_to_snake_case(input):
    snake_case = "".join(["_" + i.lower() if i.isupper() else i for i in input]).lstrip(
        "_"
    )
    return snake_case


if __name__ == "__main__":
    main()

def main():
    string = input("Please enter your text: ")
    strng = shorten(string)
    print(strng)


def shorten(string: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    for letter in string:
        if letter.lower() in vowels:
            string = string.replace(letter, "")
    return string


if __name__ == "__main__":
    main()

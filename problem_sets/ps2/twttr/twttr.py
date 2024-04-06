def main():
    string = input("Please enter your text: ")
    strng = remove_vowels(string)
    print(strng)


def remove_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    for letter in string:
        if letter.lower() in vowels:
            string = string.replace(letter, "")
    return string


if __name__ == "__main__":
    main()

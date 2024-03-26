def main():
    message = input("Send a message: ")
    convert(message)


def convert(message):
    output = str(message).replace(":)", "🙂").replace(":(", "🙁")
    print(output)


if __name__ == "__main__":
    main()

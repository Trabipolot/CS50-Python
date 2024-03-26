import pyfiglet
import sys
import random

supported_fonts = pyfiglet.FigletFont.getFonts()


def main():
    font = check_input()
    text = input("enter your text: ").strip()
    converted_text = change_font(text=text, font=font)
    print(converted_text)


def check_input():
    arguments = sys.argv
    if (
        len(arguments) == 3
        and arguments[1] in ["-f", "--font"]
        and arguments[2] in supported_fonts
    ):
        return arguments[2]
    elif len(arguments) == 1:
        return "random"
    else:
        print(
            "Invalid Input. Please adjust arguments toteh following format: -f/--font 'supported font'"
        )
        sys.exit()


def change_font(text, font):
    if font == "random":
        return pyfiglet.figlet_format(text, random.choice(supported_fonts))
    else:
        return pyfiglet.figlet_format(text, font)


if __name__ == "__main__":
    main()

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    m = re.findall(r"(^um$)|(^um[, .!?;:\"])|( um[, .!?;:\"])", s, re.IGNORECASE)
    return len(m)


if __name__ == "__main__":
    main()

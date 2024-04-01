import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if m := re.match(
        r"^<iframe .*\"https?://(?:www\.)?youtube\.com/embed/([^\"]*)\".*></iframe>",
        s,
        re.IGNORECASE,
    ):
        url = f"https://youtu.be/{m.group(1)}"
        return url
    else:
        return None


if __name__ == "__main__":
    main()
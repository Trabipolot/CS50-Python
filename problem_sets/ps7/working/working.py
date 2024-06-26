import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def adjust_hours(hour, minute, am_pm) -> str:
    hour = int(hour)
    if minute is None:
        minute = "00"
    if hour == 12 and am_pm == "AM":
        return f"00:{minute}"
    elif am_pm == "PM" and hour != 12:
        hour += 12
    return f"{hour:02}:{minute}"


def convert(s):
    if m := re.match(
        r"^([1-9]|(?:1[0-2]))(?::([0-5][0-9]))? (AM|PM) to ([1-9]|(?:1[0-2]))(?::([0-5][0-9]))? (AM|PM)$",
        s,
    ):
        time1 = adjust_hours(m.group(1), m.group(2), m.group(3))
        time2 = adjust_hours(m.group(4), m.group(5), m.group(6))
        return f"{time1} to {time2}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()

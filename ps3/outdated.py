import datetime


def main():
    date = input_date()
    print(date.strftime("%Y-%m-%d"))


def input_date():
    while True:
        date = None
        date_user = (
            input("Enter a date (Month (d)d, yyyy or mm/dd/yyyy): ").strip().title()
        )
        try:
            date = datetime.datetime.strptime(date_user, "%m/%d/%Y")
        except ValueError:
            pass
        if date is None:
            try:
                date = datetime.datetime.strptime(date_user, "%B %d, %Y")
            except ValueError:
                print("Invalid entry. Please use one of the formats specified below.")
        if date is not None:
            return date


if __name__ == "__main__":
    main()

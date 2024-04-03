from datetime import datetime, date, time
import sys
import inflect


def get_dob():
    user_input = input("Enter your date of birth: ").strip()
    try:
        dob = datetime.strptime(user_input,"%Y-%m-%d")
    except ValueError as e:
        sys.exit(e)
    return dob


def calculate_minutes(dob) -> int:
    today = datetime.combine(date.today(), time())
    diff = today - dob
    minutes = round(diff.total_seconds()/60)
    return minutes


def convert_to_words(minutes: int) ->str:
    words = inflect.engine().number_to_words(minutes).replace(" and ", " ")
    return words[0].capitalize() + words[1:]


def main():
    dob = get_dob()
    minutes = calculate_minutes(dob)
    words = convert_to_words(minutes)
    print(f"{words} minutes")

if __name__=="__main__":
    main()
    





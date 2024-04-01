from validator_collection import checkers

def check_input(user_input: str) -> bool:
    if checkers.is_email(user_input):
        return "Valid"
    else:
        return "Invalid"


def main():
    validation = check_input(input("Enter Email: ").strip())
    print(validation)

if __name__=="__main__":
    main()


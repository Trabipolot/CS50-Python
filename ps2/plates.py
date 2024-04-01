def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if not check_length(plate):
        return False
    if not check_start(plate):
        return False
    else:
        return check_order(plate)


def check_length(plate):
    return 2 <= len(plate) <= 6


def check_start(plate):
    return plate[0].isalpha() and plate[1].isalpha()


def check_order(plate):
    for i, char in enumerate(plate[2:], 2):
        if char.isdigit():
            return plate[i:].isdigit()
        elif char.isalpha():
            pass
        else:
            return False
    return True


if __name__ == "__main__":
    main()

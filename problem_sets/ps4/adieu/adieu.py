def main():
    names = collect_names()
    proper_posh_string = apply_oxford_coma(names)
    print(f"Adieu,adieu, to {proper_posh_string}")


def collect_names():
    names = []
    while True:
        try:
            item = input().strip().title()
        except EOFError:
            return names
        names.append(item)


def apply_oxford_coma(names):
    n = len(names)
    proper_posh_string = ""
    if n == 1:
        return names[0]
    elif n == 2:
        return f"{names[0]} and {names[1]}"
    else:
        for name in names[0:-1]:
            proper_posh_string += f"{name}, "
        proper_posh_string += f"and {names[-1]}"
        return proper_posh_string


if __name__ == "__main__":
    main()

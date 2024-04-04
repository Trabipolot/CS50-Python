import random


def input_number(prompt: str, min: int = -(10**10), max: int = 10**10) -> int:
    while True:
        try:
            n = int(input(prompt).strip())
            assert min <= n <= max
            return n
        except:
            print("Too large!")


def randomize(level: int) -> int:
    return random.randint(1, level)


def get_guess(level: int, random_number: int) -> bool:
    guess: int = input_number(
        f"Enter your guess (integer between 1 and {level}): ", 0, level
    )
    return check_guess(guess, random_number)


def check_guess(guess: int, random_number: int) -> bool:
    if guess == random_number:
        return True
    elif guess > random_number:
        print("Too large!")
        return False
    else:
        print("Too small!")
        return False


def main():
    validation = False
    n: int = input_number("Enter level (positive integer):", 1)
    x: int = randomize(n)
    while validation is False:
        validation: bool = get_guess(n, x)
    print("Just right!")


if __name__ == "__main__":
    main()

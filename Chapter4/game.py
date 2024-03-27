import random

def input_number(prompt: str, min: int = -(10**10), max: int = 10**10) -> int: 
    while True:
        try:
            n = int(input(prompt).strip())
            assert min <= n <= max
            return n
        except:
            print("Invalid Input")


def randomize(level: int) -> int:
    return random.randint(1,level)


def get_guess(level: int, random_number: int)-> str:
    while True:
        guess: int = input_number(f"Enter your guess (integer between 0 and {level}): ", 0, level)
        validation: str = check_guess(guess, random_number)



def check_guess(guess: int, random_number: int) -> str:
        if guess == random_number:
            return True
        elif guess > random_number:
            print("Too high!")
            return False
        else:
            print("Too low!")
            return False



def main():
    guess = False
    n: int = input_number("Enter level (positiv integer):", 0)
    x: int = randomize(n)
    while guess is False:
        guess: int = get_guess(n,x)
    print("Just right!")


if __name__=="__main__":
    main()
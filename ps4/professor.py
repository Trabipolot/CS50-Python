import random


def main():
    n: int = 0
    score: int = 0
    level: int = get_level()
    while n < 10:
        x,y= generate_integer(level)
        add_to_score = get_solution(x,y)
        if add_to_score is True:
            score += 1
        n += 1
    print(f"Score: {score} / {n}")


def get_level() ->int:
    while True:
        level: int = 0
        try:
            level: int = int(input("Level(1-3): ").strip())
        except ValueError:
            pass
        if 1 <= level <= 3:
            return level
        else:
            print("Invalid Input! Please enter number 1-3")
            


def generate_integer(level: int) -> list[int]:
    n: int = 0
    random_numbers: list = []
    while n <= 1:
        random_numbers.append(random.randint(10**(level-1),10**level-1))
        n += 1
    return random_numbers

    
def get_solution(x: int, y: int) -> bool:
    n: int = 0
    while n < 3:
        z = None
        try:
            z: int = int(input(f"{x} + {y} = ").strip())
        except:
            print("EEE")
            n += 1
        if z is not None:
            if z == x + y:
                return True
            else:
                print("EEE")
                n += 1
    print(x + y)
    return False


if __name__ == "__main__":
    main()
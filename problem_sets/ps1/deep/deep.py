def main():
    answer = input("Whats the answer to all questions?: ").strip().lower()
    if check_answer(answer):
        print("Yes")
    else:
        print("No")


def check_answer(answer):
    correct_answers = ["forty-two", "forty two", "42"]
    return answer in correct_answers


if __name__ == "__main__":
    main()

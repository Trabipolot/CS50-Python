def main():
    expression = input("Enter your Expression: ").lower().strip().split()
    result = round(calculate_expression(expression), 1)
    if not result:
        print("Invalid Input")
    else:
        print(result)


def calculate_expression(expression):
    if len(expression) == 3:
        num1, operator, num2 = expression
        try:
            num1 = float(num1)
            num2 = float(num2)
        except:
            return False
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "/" and num2 != 0:
            return num1 / num2
        elif operator == "*":
            return num1 * num2
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()

def main():
    price = 50
    accepted_coins = [5, 10, 25]
    change = coke_machine(price, accepted_coins)
    if change == 0:
        print("Enjoy your coke!")
    else:
        print(f"Here is your change of {change} cents. Enjoy your coke!")


def coke_machine(price, accepted_coins):
    while price > 0:
        try:
            coin = int(input("Insert coin: ").strip())
            if coin in accepted_coins:
                price = price - coin
                print(price)
            else:
                print("machine only accepts 5, 10 and 25 cent coins")
        except:
            print("Invalid Input")
    change = 0 - price
    return change


if __name__ == "__main__":
    main()

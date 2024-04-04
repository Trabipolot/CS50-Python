def main():
    price = 50
    accepted_coins = [5, 10, 25]
    change = coke_machine(price, accepted_coins)
    print(f"Change Owed: {change}")


def coke_machine(price, accepted_coins):
    while price > 0:
        try:
            coin = int(input("Insert coin: ").strip())
            if coin in accepted_coins:
                price = price - coin
        except:
            pass
        if price > 0:
            print(f"Amount Due: {price}")
    change = 0 - price
    return change


if __name__ == "__main__":
    main()

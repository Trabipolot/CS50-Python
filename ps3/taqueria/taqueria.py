menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    ordered_items = take_order()
    summary = order_summary(ordered_items)


def take_order():
    ordered_items = []
    while True:
        try:
            item = input("Order Item (enter cmd-d to complete order): ").title()
        except EOFError:
            print("Thanks for your order.")
            break
        if item in menu:
            ordered_items.append(item)
            price = calculate_price(ordered_items)
            print(f"Total: ${price:.2f}")
        else:
            print("Item is not on the menu, please order something else")
    return ordered_items


def calculate_price(ordered_items):
    price = float(0)
    for item in ordered_items:
        price += menu[item]
    return price


def order_summary(ordered_items):
    print("Order Summary:")
    for item in ordered_items:
        print(f"{item}:     ${menu[item]:.2f}")
    print(f"Total:      ${calculate_price(ordered_items)}")


if __name__ == "__main__":
    main()

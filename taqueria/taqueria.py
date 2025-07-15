prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
    order = []
    while True:
        try:
            items = input("Item: ").title()
            order.append(items)
            add_total(order)
        except EOFError:
            print()
            break
        except KeyError:
            pass
        except TypeError:
            pass
def add_total(order):
    values = []
    for item in order:
        price = prices[item]
        values.append(price)
        result = float(sum(values))
    print(f"Total: ${result:.2f}")

main()




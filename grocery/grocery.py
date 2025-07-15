from collections import Counter
def main():
    groceries = []
    try:
        while True:
            foods = input()
            groceries.append(foods)
    except EOFError:
        count_foods = Counter(groceries)
        food = dict(sorted(count_foods.items()))
        for foods, occurence in food.items():
            print(f"{occurence} {foods.upper()}")

main()

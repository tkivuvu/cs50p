
dollars = float(input("How much was the meal? ").replace("$", ""))
percent = float(input("What percentage would you like to tip? ").replace("%", ""))
tip = dollars * (percent / 100)
print(f"Leave ${tip:.2f}")

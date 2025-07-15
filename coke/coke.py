
amount_d = 50

while amount_d > 0:
    print("Amount Due:", amount_d)
    insert_c = int(input("Insert Coin: "))
    if insert_c == 5 or insert_c == 10 or insert_c == 25:
        amount_d = amount_d - insert_c
        continue
    elif insert_c != 5 or insert_c != 10 or insert_c != 25:
        continue

if amount_d < 0:
    print("Change Owed:", abs(amount_d))
elif amount_d == 0:
    print("Change Owed: 0")








def main():
    fraction = str(input("Fraction: "))
    x, y = str(fraction).split("/")
    x, y = int(x), int(y)
    percentage = int(x) / int(y)
    if percentage >= 0.01:
        print(gauge(percentage))
    elif percentage < 0.99:
        print(convert(fraction))
    elif percentage > 0.01:
        print(convert(fraction))
    elif percentage > 1:
        print(convert(fraction))

    else:
        print(gauge(percentage))


def convert(fraction):
    x, y = str(fraction).split("/")
    x, y = int(x), int(y)
    percentage = int(x) / int(y)
    if percentage > 1:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    elif percentage < 0.99 and percentage > 0.01:
        return int(round(percentage * 100))
    elif not isinstance(x, int):
        raise ValueError
    elif not isinstance(y, int):
        raise ValueError


def gauge(percentage):
    if percentage >= 0.99:
        return f"F"
    elif percentage <= 0.01:
        return f"E"
    elif percentage < 0.99:
        return f"{percentage}%"
    elif percentage > 0.01:
        return f"{percentage}%"


if __name__ == "__main__":
    main()



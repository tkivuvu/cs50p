import random

def main():
    mark = 0
    input_level = get_level()

    for _ in range(10):
        x = generate_integer(input_level)
        y = generate_integer(input_level)
        sum_ = x + y
        attempts = 0

        while True:
            try:
                print(f"{x} + {y} = ", end="")
                input_answer = input()
                if int(input_answer) == sum_:
                    mark = mark + 1
                    break
                else:
                    raise ValueError
            except ValueError:
                if attempts < 2:
                    print("EEE")
                    attempts = attempts + 1
                    continue
                else:
                    print(f"{x} + {y} =", sum_)
                    break
    print("Score: ", mark)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
            elif level != 1 or level != 2 or level != 3:
                raise ValueError

        except ValueError:
            continue
    return level


def generate_integer(level):
    if int(level) == 1:
        return random.randint(0, 9)
    elif int(level) == 2:
        return random.randint(10, 99)
    elif int(level) == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()

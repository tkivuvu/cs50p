import re


def main():
    s = (input("Text: ").lower())
    print(count(s))


def count(s):
    f = re.findall(r"\bum\b", s, re.IGNORECASE)

    ff = len(f)

    return f"{ff}"


if __name__ == "__main__":
    main()

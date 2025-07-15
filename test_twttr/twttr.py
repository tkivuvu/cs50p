def main():
    word = input("Input: ")
    print("Output:",(shorten(word)))



def shorten(word):
    return f"{word}".replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "").replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")


if __name__ == "__main__":
    main()


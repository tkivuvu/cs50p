def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return first_letters(s) and word_length(s) and endofword(s) and punct_mark(s)


def first_letters(word):
    if word[:2].isalpha():
        return True

def word_length(word):
    if 2 <= len(word) <= 6:
        return True

def endofword(word):
    if word.isalpha():
        return True
    else:
        middle_digit = False
        for d in word:
            if d.isdigit():
                middle_digit = True
                i = word.index(d)
                break
        if middle_digit:
            if d == "0":
                return False
            if word[i:].isdigit():
                return True
            else:
                return False

def punct_mark(word):
    return not any(d in "'.,;:?! " for d in word)

if __name__ == "__main__":
    main()

import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                continue
            elif level >= 1:
                guess_()
                break
        except ValueError:
            continue


def guess_():
    number = random.randint(1, 10)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < number:
                print("Too small!")
                continue
            elif guess > number:
                print("Too large!")
                continue
            elif guess == number:
                sys.exit("Just right!")
        except ValueError:
            continue

main()

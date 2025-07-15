def main():
    time = input("What time is it? ")
    convert(time)
    if convert(time) >= 7 and convert(time) <= 8:
        print("breakfast time")
    elif convert(time) >= 12 and convert(time) <= 13:
        print("lunch time")
    elif convert(time) >= 18 and convert(time) <= 19:
        print("dinner time")
    else:
        print("", end="")

def convert(time):
    h, m = time.split(":")
    time = (int(h) * 1) + (int(m) / 60)
    return time



if __name__ == "__main__":
    main()

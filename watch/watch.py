import re



def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r'(?:\")(?:https?://)?(?:www\.)?youtube\.com/embed/(.+?)(?:\")', s)
    if matches:
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None



if __name__ == "__main__":
    main()

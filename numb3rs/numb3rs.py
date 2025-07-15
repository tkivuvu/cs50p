

def main():
    id_ad = input("IPv4 Address: ")
    print(validate(id_ad))


def validate(id_ad):
    ip_parts = id_ad.split(".")
    try:
        if all(0 <= int(part) <= 255 for part in ip_parts) and len(ip_parts) == 4:
            return True

        else:
            return False
    except ValueError:
        return False



if __name__ == "__main__":
    main()

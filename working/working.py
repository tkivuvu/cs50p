import re


def main():
    s = input("Hours: ")
    print(convert(s))

def convert(s):
    matches = re.search(r"(1[0-2]|[1-9])(?:\:)?([0-5][0-9])? (AM|PM) (?:to) (1[0-2]|[1-9])(?:\:)?([0-5][0-9])? (AM|PM)", s)

    if matches:
        hr1 = matches.group(1)
        min1 = matches.group(2)
        am_pm1 = matches.group(3)
        hr2 = matches.group(4)
        min2 = matches.group(5)
        am_pm2 = matches.group(6)
        a = 12
        hr1 = int(hr1)
        hr2 = int(hr2)

        if hr1 < 10 and am_pm1 == "AM" and am_pm2 == "PM" and hr2 != 12 and min1 != None and min2 != None:
            return f"0{hr1}:{min1} to {hr2 + a}:{min2}"

        elif hr1 > 10 and am_pm1 == "AM" and am_pm2 == "PM" and hr2 != 12 and min1 != None and min2 != None:
            return f"{hr1}:{min1} to {hr2 + a}:{min2}"

        elif hr1 < 10 and am_pm1 == "AM" and am_pm2 == "PM" and hr2 != 12 and min1 == None and min2 != None:
            return f"0{hr1}:00 to {hr2 + a}:{min2}"

        elif hr1 > 10 and am_pm1 == "AM" and am_pm2 == "PM" and hr2 != 12 and min1 == None and min2 != None:
            return f"{hr1}:00 to {hr2 + a}:{min2}"

        elif hr1 < 10 and am_pm1 == "AM" and am_pm2 == "PM" and hr2 != 12 and min1 != None and min2 == None:
            return f"0{hr1}:{min1} to {hr2 + a}:00"

        elif hr1 > 10 and am_pm1 == "AM" and am_pm2 == "PM" and hr2 != 12 and min1 != None and min2 == None:
            return f"{hr1}:{min1} to {hr2 + a}:00"

        elif hr1 < 10 and am_pm1 == "AM" and am_pm2 == "PM" and hr2 != 12 and min1 == None and min2 == None:
            return f"0{hr1}:00 to {hr2 + a}:00"

        elif hr1 > 10 and am_pm1 == "AM" and am_pm2 == "PM" and hr2 != 12 and min1 == None and min2 == None:
            return f"{hr1}:00 to {hr2 + a}:00"

        elif hr2 < 10 and am_pm1 == "PM" and am_pm2 == "AM" and hr1 != 12 and min1 != None and min2 != None:
            return f"{hr1 + a}:{min1} to 0{hr2}:{min2}"

        elif hr2 > 10 and am_pm1 == "PM" and am_pm2 == "AM" and hr1 != 12 and min1 != None and min2 != None:
            return f"{hr1 + a}:{min1} to {hr2}:{min2}"

        elif hr2 < 10 and am_pm1 == "PM" and am_pm2 == "AM" and hr1 != 12 and min1 == None and min2 != None:
            return f"{hr1 + a}:00 to 0{hr2}:{min2}"

        elif hr2 > 10 and am_pm1 == "PM" and am_pm2 == "AM" and hr1 != 12 and min1 == None and min2 != None:
            return f"{hr1 + a}:00 to {hr2}:{min2}"

        elif hr2 < 10 and am_pm1 == "PM" and am_pm2 == "AM" and hr1 != 12 and min1 != None and min2 == None:
            return f"{hr1 + a}:{min1} to 0{hr2}:00"

        elif hr2 > 10 and am_pm1 == "PM" and am_pm2 == "AM" and hr1 != 12 and min1 != None and min2 == None:
            return f"{hr1 + a}:{min1} to {hr2}:00"

        elif hr2 < 10 and am_pm1 == "PM" and am_pm2 == "AM" and hr1 != 12 and min1 == None and min2 == None:
            return f"{hr1 + a}:00 to 0{hr2}:00"

        elif hr2 > 10 and am_pm1 == "PM" and am_pm2 == "AM" and hr1 != 12 and min1 == None and min2 == None:
            return f"{hr1 + a}:00 to {hr2}:00"




        elif hr2 == 12 and am_pm1 == "AM" and am_pm2 == "PM" and hr1 == 12 and min1 != None and min2 != None:
            return f"0{hr1 - a}:{min1} to {hr2}:{min2}"
        elif hr2 == 12 and am_pm1 == "AM" and am_pm2 == "PM" and hr1 == 12 and min1 == None and min2 != None:
            return f"0{hr1 - a}:00 to {hr2}:{min2}"
        elif hr2 == 12 and am_pm1 == "AM" and am_pm2 == "PM" and hr1 == 12 and min1 != None and min2 == None:
            return f"0{hr1 - a}:{min1} to {hr2}:00"
        elif hr2 == 12 and am_pm1 == "AM" and am_pm2 == "PM" and hr1 == 12 and min1 == None and min2 == None:
            return f"0{hr1 - a}:00 to {hr2}:00"


        elif hr1 == 12 and am_pm1 == "PM" and am_pm2 == "AM" and hr2 == 12 and min1 != None and min2 != None:
            return f"{hr1}:{min1} to 0{hr2 - a}:{min2}"
        elif hr1 == 12 and am_pm1 == "PM" and am_pm2 == "AM" and hr2 == 12 and min1 == None and min2 != None:
            return f"{hr1}:00 to 0{hr2 - a}:{min2}"
        elif hr1 == 12 and am_pm1 == "PM" and am_pm2 == "AM" and hr2 == 12 and min1 != None and min2 == None:
            return f"{hr1}:{min1} to 0{hr2 - a}:00"
        elif hr1 == 12 and am_pm1 == "PM" and am_pm2 == "AM" and hr2 == 12 and min1 == None and min2 == None:
            return f"{hr1}:00 to 0{hr2 - a}:00"


    else:
        raise ValueError


if __name__ == "__main__":
    main()



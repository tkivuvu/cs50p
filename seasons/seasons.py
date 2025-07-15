from datetime import date
import inflect
import sys


def main():
    s = input("Date of Birth: ")
    print(dob(s))


def dob(s):
    try:
        p = inflect.engine()
        year, month, day = s.split("-")
        year, month, day = int(year), int(month), int(day)
        today = date.today()
        date1 = date(year, month, day)
        difference = today - date1
        total_minutes = difference.total_seconds() / 60
        total_minutes = round(total_minutes)
        total_minutes1 = p.number_to_words(total_minutes)
        total_minutes1 = total_minutes1.replace(" and", "").capitalize()
        return f"{total_minutes1} minutes"
    except (ValueError):
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()

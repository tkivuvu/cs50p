import csv
import sys
try:
    with open (sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        if len(sys.argv) != 3:
            sys.exit("too many or too little command-line arguments")
        elif len(sys.argv) == 3:
            with open (sys.argv[2], "w") as newfile:
                    fieldnames = ["first", "last", "house"]
                    writer = csv.DictWriter(newfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for row in reader:
                        r = row["name"].split(", ")
                        writer.writerow({"first": r[1], "last": r[0], "house": row["house"]})
except FileNotFoundError:
    sys.exit("not suitable")


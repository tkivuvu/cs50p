import sys
from tabulate import tabulate
import csv


try:
    with open(sys.argv[1]) as file:
        if sys.argv[1] == "sicilian.csv":
            print(tabulate({"Sicilian Pizza": ["Cheese", "1 item", "2 items", "3 items", "Special"],
                        "Small": ["$25.50", "$27.50", "$29.50","$31.50","$33.50"],
                        "Large": ["$39.95", "$41.95", "$43.95", "$45.95", "$47.95"]
                                  }, headers="keys", tablefmt="grid"))
        elif sys.argv[1] == "regular.csv":
                print(tabulate({"Regular Pizza": ["Cheese", "1 topping", "2 toppings", "3 toppings", "Special"],
                        "Small": ["$13.50", "$14.75", "$15.95","$16.95","$18.50"],
                        "Large": ["$18.95", "$20.95", "$22.95", "$24.95", "$26.95"]
                                  }, headers="keys", tablefmt="grid"))
        elif not sys.argv[1].endswith(".csv"):
            sys.exit("not a csv file")
        elif len(sys.argv) > 2:
            sys.exit("too many lines of argument")
except (FileNotFoundError, IndexError):
    sys.exit("file does not exist or too many or few lines of argument")

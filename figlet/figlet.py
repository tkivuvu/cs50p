import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    Input = input("Input: ")
    f = figlet.getFonts()
    figlet = Figlet(font=random.choice(f))
    print("Output: ", figlet.renderText(Input))
elif len(sys.argv) < 3:
    sys.exit("Invalid usage")
elif sys.argv[2] not in figlet.getFonts():
    sys.exit("Invalid usage")
elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
    Input = input("Input: ")
    figlet = Figlet(font=sys.argv[2])
    print("Output: ", figlet.renderText(Input))
elif sys.argv[1] != "-f" or sys.argv[1] != "--font":
    sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")




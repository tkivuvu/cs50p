import sys



try:
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
        if not sys.argv[1].endswith(".py"):
            sys.exit("not a python file")
        elif len(sys.argv) > 2:
            sys.exit("too may lines of argument")


except (FileNotFoundError, IndexError):
    sys.exit("file does not exist or too many or few lines of argument")

count = 0
for line in lines:
    stripped_line = line.strip()
    if stripped_line != "" and not stripped_line.startswith('#'):
        count += 1

print(count)

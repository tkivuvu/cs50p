import sys
from PIL import Image, ImageOps
import os


try:
    length = len(sys.argv)
    ext1 = os.path.splitext(sys.argv[1])[1]
    ext2 = os.path.splitext(sys.argv[2])[1]
    if length > 3:
        sys.exit("too many lines of argument")
    elif length < 3:
        sys.exit("too few lines of argument")
    elif ext1 != ext2:
        sys.exit("extensions are not matching")
    elif ext1 not in [".jpg", ".jpeg", ".png"]:
        sys.exit("not the right extension")
    elif ext2 not in [".jpg", ".jpeg", ".png"]:
        sys.exit("not the right extension")
    else:
        photo = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        size = (600, 600)
        new_img = ImageOps.fit(photo, size, bleed=0.0, centering=(0.5,0.5))
        new_img.paste(shirt, shirt)
        new_img.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("input file does not exist")

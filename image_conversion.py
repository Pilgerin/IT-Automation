#!/usr/bin/env python3
import glob
import os
from PIL import Image

for root, dirs, files in os.walk("."):
    for file in files:
        f, e = os.path.splitext(file)
        outfile = "/opt/icons/" + f
        try:
            Image.open(file).rotate(270).resize((128, 128)).convert("RGB").save(outfile, "JPEG")

        except IOError:
            print("cannot convert", file)

for img in glob.glob('*'):
    if img.endswith(".py"):
        continue
    im = Image.open(img).convert('RGB')
    new_im = im.rotate(270).resize((128, 128)).save("/opt/icons/" + str(img) + ".jpg")
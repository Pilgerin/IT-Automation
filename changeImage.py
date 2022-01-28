#!/usr/bin/env python3
import os
from PIL import Image

path = 'supplier-data/images/'
pictures = os.listdir(path)

for infile in pictures:
    if not infile.startswith('.') and 'tiff' in infile:
        stripped_filename = os.path.splitext(infile)[0]
        im_out = path + stripped_filename + ".jpeg"
        im = Image.open(path + infile)
        im.convert('RGB').resize((600, 400)).save(im_out, 'jpeg')
        im.close()

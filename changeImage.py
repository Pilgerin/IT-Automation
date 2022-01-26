#!/usr/bin/env python3
import os, sys
from PIL import Image

path = os.getcwd()
path_in = path + '/supplier-data/images/'

for infile in os.listdir(path_in):
    if not infile.startswith('.') and 'tiff' in infile:
        im = Image.open(path_in + infile)
        im.convert('RGB').resize((600, 400)).save(path_in + infile, 'jpeg')
        im.close()

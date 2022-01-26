#!/usr/bin/env python3
import os, sys
from PIL import Image

path = os.getcwd()
path_in = path + '/supplier-data/images/'

# if not os.path.exists(path_out):
#   os.makedirs(path_out)
# if new folder doesn't exist, create it


for infile in os.listdir(path_in):
    if not infile.startswith('.'):
        im = Image.open(path_in + infile)
        im.convert('RGB').resize((600, 400)).save(path_in + infile, 'jpeg')
        im.close()

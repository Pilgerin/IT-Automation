#!/usr/bin/env python3
import os,sys
from PIL import Image

path  = os.getcwd()

path_in = path + '/images/'
path_out =  '/opt/icons/'
#one level higher, not on the same level

if not os.path.exists(path_out):
    os.makedirs(path_out)
#if new folder doesn't exist, create it


for infile in os.listdir(path_in):
    if not infile.startswith('.'):
        im = Image.open(path_in+infile)
        im.rotate(270).convert('RGB').resize((128, 128)).save(path_out + infile, 'jpeg')
        im.close()


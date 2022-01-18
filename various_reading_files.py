#!/usr/bin/env python3
import os,sys
from PIL import Image
import glob

print('Named explicitly:')
for name in glob.glob('/home/geeks/Desktop/gfg/data.txt'):
    print(name)

# Using '*' pattern
print('\nNamed with wildcard *:')
for name in glob.glob('/home/geeks/Desktop/gfg/*'):
    print(name)

# Using '?' pattern
print('\nNamed with wildcard ?:')
for name in glob.glob('/home/geeks/Desktop/gfg/data?.txt'):
    print(name)

# Using [0-9] pattern
print('\nNamed with wildcard ranges:')
for name in glob.glob('/home/geeks/Desktop/gfg/*[0-9].*'):
    print(name)

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


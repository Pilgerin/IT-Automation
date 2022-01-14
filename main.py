import os, sys
from PIL import Image

path = os.getcwd()
#gets current working directory
path_in = path + '/images/'
path_out = '/opt/icons/'
#one level higher, not on the same level

if not os.path.exists(path_out):
    os.makedirs(path_out)
#if new folder doesn't exist, create it


def modify_images(save_path):
    for infile in path_in:
        if not infile.startswith('.'):
            with Image.open(infile) as im:
                print(infile, im.format, f"{im.size}x{im.mode}")
                im.rotate(270).convert('RGB').resize((128, 128)).save(path_out,".jpg")
            im.close()

if __name__ == '__main__':
    modify_images(path_in)

#!/usr/bin/env python3
import os
import requests

from multiprocessing import Pool

path_in = os.listdir('/supplier-data/images')
#Django needs trailing slash!
url = 'http://[linux-instance-IP-Address]/media/images/'
multiple_files = []
for img in path_in:
    # traverses each file in the directory
    if not img.startswith('.'):
        with open("/supplier-data/images" + img) as fb:
            multiple_files.extend(('images', ('img.jpg', open(img, 'rb'), 'image/png')))
            r = requests.post(url, data=multiple_files)
print(r.text)
print(r.status_code)

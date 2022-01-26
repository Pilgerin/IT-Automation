#!/usr/bin/env python3
import os
import requests

path_in = os.listdir('/supplier-data/images')
url = 'http://[linux-instance-IP-Address]/media/images/'
# Django needs trailing slash!
for img in path_in:
    # traverses each file in the directory
    if not img.startswith('.') and "jpeg" in img:
        with open(path_in + img, 'rb') as fb:
            r = requests.post(url, files={'file': fb})
print(r.text)
print(r.status_code)

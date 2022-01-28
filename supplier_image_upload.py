#!/usr/bin/env python3
import os
import requests

path = 'supplier-data/images/'
images = os.listdir(path)
url = 'http://localhost/upload/'
# Django needs trailing slash!
for img in images:
    # traverses each file in the directory
    if img.endswith(".jpeg"):
        with open(path + img, 'rb') as fb:
            r = requests.post(url, files={'file': fb})
            print(r.text)
            print(r.status_code)

'''#!/usr/bin/env python3
import requests

url = "http://localhost/upload/"
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})
'''

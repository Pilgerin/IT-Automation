#! /usr/bin/env python3
import os
import requests
import json


def catalog_creation(localpath, description_url):
    descriptions = os.listdir(localpath)
    for file in descriptions:
        # traverses each file in the directory
        if file.endswith('.txt'):
            with open(localpath + file) as fb:
                fruit = os.path.splitext(file)[0]
                description = fb.read().split('\n')
                print(description)
                line_dict = {'name': description[0], 'weight': int(description[1].strip('lbs')),
                             'description': description[2],
                             'image name': fruit + '.jpeg'}
                print(line_dict)
                r = requests.post(url, json=line_dict)
                print(r.text)
                print(r.status_code)
    return 0


if __name__ == '__main__':
    path = 'supplier-data/descriptions/'
    url = 'http://localhost/fruits/'
    catalog_creation(path, url)

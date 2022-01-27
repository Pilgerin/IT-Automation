#! /usr/bin/env python3
import os
import requests
import json


def catalog_creation(filename, description_url):
    for fdbck in path_in:
        # traverses each file in the directory
        fields = ['name', 'weight', 'description', 'image name']
        if not fdbck.startswith('.'):
            with open("/supplier-data/descriptions" + fdbck) as fb:
                description = fb.read().split('\n')
                print(description)
                line_dict = {'name': description[0], 'weight': int(description[1].strip('lbs')),
                             'description': description[2],
                             'image name': os.path.basename('/supplier-data/images' + fdbck.strip('txt') + 'jpeg')}
                r = requests.post(url, data=line_dict)
            with open('report.txt', 'w') as convert_file:
                convert_file.write(json.dumps(line_dict))
    print(r.text)
    print(r.status_code)
    return 0


if __name__ == '__main__':
    path_in = os.listdir('/supplier-data/descriptions')
    url = 'http://[linux-instance-IP-Address]/media/fruits/'
    catalog_creation(path_in, url)

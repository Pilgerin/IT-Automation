#! /usr/bin/env python3
import os
import requests

path_in = '/data/feedback'
file_traversal = [i for i in os.walk(path_in)][0][2]
dict = {}
for fdbck in file_traversal:
    # traverses each file in the directory
    print(fdbck)
    fields = ['title', 'name', 'date', 'feedback']
    if not fdbck.startswith('.'):
        with open(fdbck) as fb:
            l = 1
            # count for id of each dict in the dict
            for line in fb.readlines():
                description = list(line.strip().split(None, 4))
                print(description)
                id = 'feed' + str(l)
                i = 0
                line_dict = {}
                while i < len(fields):
                    # intermediate dict for each feedback
                    line_dict[fields[i]] = description[i]
                    i = i + 1
                dict[id] = line_dict
                l = l + 1
url = 'http://IP/feedback/'
r = requests.post(url, json=dict)
print(r.text)
print(r.status_code)

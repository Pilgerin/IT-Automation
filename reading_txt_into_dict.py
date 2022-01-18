#! /usr/bin/env python3
import os
import requests
from multiprocessing import Pool

path_in = os.listdir('/data/feedback')
#Django needs trailing slash!
url = 'http://34.133.246.94/feedback/'
for fdbck in path_in:
    # traverses each file in the directory
    fields = ['title', 'name', 'date', 'feedback']
    if not fdbck.startswith('.'):
        with open("/data/feedback/" + fdbck) as fb:
            description = fb.read().split('\n')
            print(description)
            line_dict = {'title':description[0],'name':description[1],'date':description[2],'feedback':description[3]}
            r = requests.post(url, data=line_dict)
        '''alternatively:
        fp = open('/data/feedback/' + file)
        data = fp.read().split('\n')
        dic = {"title": data[0], "name": data[1], "date": data[2], "feedback": data[3]}
        response = requests.post(url, json=dic)
        '''
print(r.text)
print(r.status_code)

'''
utilizes Multiprocessing
tasks = [i for i in os.walk(path_in)][0][2]

def run(task):
    if not task.endswith(".txt"): return None
    try:
        file = dr + task
        with open(file) as f:
            text = [i.strip() for i in f.readlines()]
        data = {"title": text[0], "name": text[1], "date": text[2], "feedback": text[3]}
        req = requests.post("http://34.121.32.234/feedback/", json=data)
        req.raise_for_status()

    except Exception as e:
        print(task, e)

p = Pool(len(tasks))
p.map(run, tasks)'''
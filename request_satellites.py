'''
This is the best approach (so far) to request satellite data. 

One request returns json with more than 20 000 satellites.

Ange is resposoble for how many satellites will be requested. 1 returns smallest possible amount, 180 returns
everything.

'''

import requests
import os
from dotenv import load_dotenv
import csv

load_dotenv()


key = os.environ.get('TOKEN')

angle = 180


def get_sat_count(angle, key):
    r = requests.get(f'https://api.n2yo.com/rest/v1/satellite/above/0/0/0/{angle}/0/&apiKey={key}')
    sat_count = r.json()['info']['satcount']
    return sat_count


def make_request(angle, key):
    r = requests.get(f'https://api.n2yo.com/rest/v1/satellite/above/0/0/0/{angle}/0/&apiKey={key}')
    return r.json()


def write_csv(data):
    with open('database.csv','a', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', lineterminator = '\n')
        writer.writerows(data)


data = make_request(angle, key)



for i, item in enumerate(data['above']):
    name = data['above'][i]['satname']
    lat = data['above'][i]['satlat']
    long = data['above'][i]['satlng']
    alt = data['above'][i]['satalt'] 
    satid = data['above'][i]['satid']
    print(name)
'''
This is the best approach (so far) to request satellite data. 

One request returns json with more than 20 000 satellites.

Ange is resposoble for how many satellites will be requested. 1 returns smallest possible amount, 180 returns
everything.

for some reason dict saves less data???

'''

import requests
import os
from dotenv import load_dotenv
import csv

load_dotenv()


key = os.environ.get('TOKEN')

angle = 360


def get_sat_count(angle, key):
    r = requests.get(f'https://api.n2yo.com/rest/v1/satellite/above/0/0/0/{angle}/0/&apiKey={key}')
    sat_count = r.json()['info']['satcount']
    return sat_count


def make_request(angle, key):
    r = requests.get(f'https://api.n2yo.com/rest/v1/satellite/above/0/0/0/{angle}/0/&apiKey={key}')
    return r.json()


def write_csv_dict(data):
    with open('database_dict.csv','w', encoding='utf-8') as f:
        for key in data.keys():
            f.write("%s, %s\n" % (key, data[key]))


def write_to_csv_list(data):
    with open('database_list.csv','w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


data = make_request(angle, key)




def filter_data(data):
    satellites = {}
    names = []
    for i, _ in enumerate(data['above']):
        name = data['above'][i]['satname']
        satid = data['above'][i]['satid']
        # lat = data['above'][i]['satlat']
        # long = data['above'][i]['satlng']
        # alt = data['above'][i]['satalt'] 
        satellites = {**satellites, name:satid}
        # names.append([name])
    # return names
    return satellites

# print(filter_data(data))

write_csv_dict(filter_data(data))

# write_to_csv_list(filter_data(data))
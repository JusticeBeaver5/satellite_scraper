'''
This method for requesting specific satellite position

'''

import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

key = os.environ.get('TOKEN')

sat_id = 25544

url = f'https://api.n2yo.com/rest/v1/satellite/positions/{sat_id}/0/0/0/2/&apiKey={key}'


def request_sat_pos(url, sat_id):
    r = requests.get(url)
    # print(r.json())
    name = r.json()['info']['satname']
    lat = r.json()['positions'][0]['satlatitude']
    lon = r.json()['positions'][0]['satlongitude']
    alt = r.json()['positions'][0]['sataltitude']
    return [name, lat, lon, alt]

while True:
    print(request_sat_pos(url))


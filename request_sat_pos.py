import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

key = os.environ.get('TOKEN')


url = f'https://api.n2yo.com/rest/v1/satellite/positions/25544/0/0/0/2/&apiKey={key}'



 # retrieve starlinks № 52 in categ id from here https://www.n2yo.com/api/
starlinks = f'https://api.n2yo.com/rest/v1/satellite/above/0/0/0/180/52/&apiKey={key}'

all = f'https://api.n2yo.com/rest/v1/satellite/above/0/0/0/180/0/&apiKey={key}'



def request_sat_pos(url):
    r = requests.get(url)
    # print(r.json())
    name = r.json()['info']['satname']
    lat = r.json()['positions'][0]['satlatitude']
    lon = r.json()['positions'][0]['satlongitude']
    alt = r.json()['positions'][0]['sataltitude']
    return [name, lat, lon, alt]


print(request_sat_pos(url))

# while True:
    # print(request_sat_pos(url))


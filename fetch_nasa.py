import requests
import os
from pathlib import Path
import urllib.parse 
import datetime


def load_image(url, filename, dirname):
    os.chdir(dirname)

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)
    
    os.chdir('../.')


def get_type_image(url):
    result = urllib.parse.urlsplit(url).path
    result = urllib.parse.unquote(result)
    result = os.path.splitext(result)
    return result[1]


def fetch_nasa_apod(dirname):

    Path(dirname).mkdir(parents=True, exist_ok=True)

    url = 'https://api.nasa.gov/planetary/apod'

    payload = {
        'count': 30,
        'api_key': os.getenv('TOKEN')
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    answer = response.json()
    for image_number, image_link in enumerate(answer):
        link = get_type_image(image_link['url'])
        load_image(image_link['url'], f'Nasa{image_number}{link}', 'images')


def fetch_nasa_epic(dirname):
    Path(dirname).mkdir(parents=True, exist_ok=True)

    url = f'https://api.nasa.gov/EPIC/api/natural/images'

    payload = {
        'api_key': os.getenv('TOKEN')
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    answer = response.json()

    for i in range(len(answer)):
        item = answer[i]
        item_date = datetime.datetime.fromisoformat(item['date'])
        item_name = item['image']
        token = os.getenv('TOKEN')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{item_date.year}/{item_date.month}/{item_date.day}/png/{item_name}.png?api_key={token}'
        load_image(url, f'{item_name}.png', 'images')

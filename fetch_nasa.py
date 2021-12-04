import requests
import os
import urllib.parse 
import datetime
import load_files as lf


def get_type_image(url):
    result = urllib.parse.urlsplit(url).path
    result = urllib.parse.unquote(result)
    result = os.path.splitext(result)
    return result[1]


def fetch_nasa_apod(dirname, api_key):

    lf.path_check(dirname)

    url = 'https://api.nasa.gov/planetary/apod'

    payload = {
        'count': 30,
        'api_key': api_key
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    answer = response.json()
    for image_number, image_link in enumerate(answer):
        link = get_type_image(image_link['url'])
        lf.load_image(image_link['url'], f'Nasa{image_number}{link}', 'images')


def fetch_nasa_epic(dirname, api_key):
    
    lf.path_check(dirname)

    url = f'https://api.nasa.gov/EPIC/api/natural/images'

    payload = {
        'api_key': api_key
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    answer = response.json()

    for ans in answer:
        item = ans
        item_date = datetime.datetime.fromisoformat(item['date'])
        item_name = item['image']
        token = os.getenv('TOKEN')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{item_date.year}/{item_date.month}/{item_date.day}/png/{item_name}.png?api_key={token}'
        params = urllib.parse.urlparse(url)
        new_url = urllib.parse.urlencode(params)
        lf.load_image(new_url, f'{item_name}.png', 'images')

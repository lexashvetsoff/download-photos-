import requests
import os
import urllib.parse 
import datetime
import load_files as lf


def get_extension(url):
    result = urllib.parse.urlsplit(url).path
    result = urllib.parse.unquote(result)
    result = os.path.splitext(result)
    return result[1]


def fetch_nasa_apod(dirname, api_key):

    url = 'https://api.nasa.gov/planetary/apod'

    payload = {
        'count': 30,
        'api_key': api_key
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    answer = response.json()
    for image_number, image_link in enumerate(answer):
        link = get_extension(image_link['url'])
        lf.load_image(image_link['url'], f'Nasa{image_number}{link}', dirname)


def fetch_nasa_epic(dirname, api_key):

    url = f'https://api.nasa.gov/EPIC/api/natural/images'

    payload = {
        'api_key': api_key
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    answer = response.json()

    for ans in answer:
        ans_date = datetime.datetime.fromisoformat(ans['date'])
        ans_name = ans['image']
        token = api_key
        attributes_url = urllib.parse.urlparse(f'https://api.nasa.gov/EPIC/archive/natural/{ans_date.year}/{ans_date.month}/{ans_date.day}/png/{ans_name}.png')
        attributes_url.params = f'api_key={token}'
        url = urllib.parse.urlparse(attributes_url)
        lf.load_image(url, f'{ans_name}.png', dirname)

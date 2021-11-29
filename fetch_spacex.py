import requests
import os
from pathlib import Path


def load_image(url, filename, dirname):
    os.chdir(dirname)

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)
    
    os.chdir('../.')



def fetch_spacex_last_launch(dirname):

    Path(dirname).mkdir(parents=True, exist_ok=True)

    url = 'https://api.spacexdata.com/v4/launches'

    response = requests.get(url)
    response.raise_for_status()

    answer = response.json()[93]

    for image_number, image_link in enumerate(answer['links']['flickr']['original']):
        load_image(image_link, f'Space{image_number}.jpg', dirname)
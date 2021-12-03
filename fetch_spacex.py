import requests
from pathlib import Path
import load_files as lf


def fetch_spacex_last_launch(dirname):

    Path(dirname).mkdir(parents=True, exist_ok=True)

    url = 'https://api.spacexdata.com/v4/launches'

    response = requests.get(url)
    response.raise_for_status()

    answer = response.json()[93]

    for image_number, image_link in enumerate(answer['links']['flickr']['original']):
        lf.load_image(image_link, f'Space{image_number}.jpg', dirname)
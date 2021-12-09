import requests
import load_files as lf


def fetch_spacex_last_launch(dirname):
    flight_number = 93

    url = 'https://api.spacexdata.com/v4/launches'

    response = requests.get(url)
    response.raise_for_status()

    answer = response.json()[flight_number]

    for image_number, image_link in enumerate(answer['links']['flickr']['original']):
        lf.load_image(image_link, f'Space{image_number}.jpg', dirname)
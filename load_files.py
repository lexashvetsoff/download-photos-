import requests
import os


def load_image(url, params, filename, dirname):
    path = os.path.join(dirname, filename)

    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)

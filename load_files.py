import requests
import os
from pathlib import Path


def load_image(url, filename, dirname):
    path = os.path.join(dirname, filename)

    response = requests.get(url)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)


def path_check(dirname):
    Path(dirname).mkdir(parents=True, exist_ok=True)
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


def path_check(dirname):
     Path(dirname).mkdir(parents=True, exist_ok=True)
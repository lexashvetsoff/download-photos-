import requests
import os


def load_image(url, filename, dirname):
    os.chdir(dirname)

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)
    
    os.chdir('../.')
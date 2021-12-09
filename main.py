import os
from dotenv import load_dotenv
import telegram
import time
import fetch_nasa
import fetch_spacex
import shutil
from pathlib import Path


def get_filepaths(path):
    filepaths = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            filepaths.append(os.path.join(path, file))
    return filepaths


def main():
    load_dotenv()
    nasa_api_key = os.getenv('NASA_TOKEN')
    bot = telegram.Bot(token=os.getenv('TG_TOKEN'))

    Path('images').mkdir(parents=True, exist_ok=True)

    while True:
        fetch_spacex.fetch_spacex_last_launch('images')
        fetch_nasa.fetch_nasa_epic('images', nasa_api_key)
        fetch_nasa.fetch_nasa_apod('images', nasa_api_key)

        filepaths = get_filepaths('images')

        for filepath in filepaths:
            with open(filepath, 'rb') as new_file:
                bot.send_photo(chat_id=os.getenv('tg_chat_id'), photo=new_file)
            time.sleep(int(os.getenv('sleep')))

        shutil.rmtree('images', ignore_errors=False, onerror=None)


if __name__ == '__main__':
    main()
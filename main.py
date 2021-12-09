import os
from dotenv import load_dotenv
import telegram
import time
import fetch_nasa
import fetch_spacex
import shutil


def get_filepaths(path):
    filepaths = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            filepaths.append(file)
    return filepaths


def main():
    load_dotenv()
    api_key = os.getenv('TOKEN')
    bot = telegram.Bot(token=os.getenv('TG_TOKEN'))

    while True:
        fetch_spacex.fetch_spacex_last_launch('images')
        fetch_nasa.fetch_nasa_epic('images', api_key)
        fetch_nasa.fetch_nasa_apod('images', api_key)

        filepaths = get_filepaths('images')

        os.chdir('images')

        for filepath in filepaths:
            with open(filepath, 'rb') as new_file:
                bot.send_photo(chat_id=os.getenv('chat_id'), photo=new_file)
            time.sleep(int(os.getenv('sleep')))
        
        os.chdir('../.')

        shutil.rmtree('images', ignore_errors=False, onerror=None)


if __name__ == '__main__':
    main()
import os
from dotenv import load_dotenv
import telegram
import time
import fetch_nasa
import fetch_spacex
import shutil


def get_files(my_path):
    list_files = []
    for file in os.listdir(my_path):
        if os.path.isfile(os.path.join(my_path, file)):
            list_files.append(file)
    return list_files


def main():
    load_dotenv()
    bot = telegram.Bot(token=os.getenv('TG_TOKEN'))

    while True:
        fetch_spacex.fetch_spacex_last_launch('images')
        fetch_nasa.fetch_nasa_apod('images')
        fetch_nasa.fetch_nasa_epic('images')

        files_list = get_files('images')

        os.chdir('images')

        for file in files_list:
            with open(file, 'rb') as my_file:
                bot.send_photo(chat_id=os.getenv('chat_id'), photo=my_file)
            time.sleep(int(os.getenv('sleep')))
        
        os.chdir('../.')

        shutil.rmtree('images', ignore_errors=False, onerror=None)


if __name__ == '__main__':
    main()
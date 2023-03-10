import telegram
import os
from dotenv import load_dotenv
import time
import argparse
from random import choice


def publish_photos_in_loop(path, delay_in_hours, token, chat_id):
    if not os.path.isabs(path):  # relative path case
        path = f'{os.path.dirname(os.path.abspath(__file__))}/{path}'

    delay_in_seconds = float(delay_in_hours) * 3600
    filesindir = os.listdir(path=path)
    bot = telegram.Bot(token=token)
    while True:
        filename = choice(filesindir)
        with open(f'{path}/{filename}', 'rb') as file:
            bot.send_document(
                chat_id=chat_id,
                document=file
                )
        filesindir.remove(filename)
        if not filesindir:
            filesindir = os.listdir(path=path)
        time.sleep(delay_in_seconds)


def main():
    load_dotenv()
    token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHANNEL_ID']

    parser = argparse.ArgumentParser(
        description='Upload photos to Telegram channel in endless loop'
    )
    parser.add_argument(
        '-d', '--delay', default=4,
        help='set upload delay in hours. You can enter a floating point number'
        )
    parser.add_argument(
        'path', help='enter the path from which you want to publish photos')
    args = parser.parse_args()
    path = args.path
    delay = args.delay

    publish_photos_in_loop(path, delay, token, chat_id)


if __name__ == "__main__":
    main()

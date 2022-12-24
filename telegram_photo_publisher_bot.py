import telegram
import os
from dotenv import load_dotenv
import time
import argparse
from random import shuffle
from random import choice


def publish_photo_by_tgbot(path, delay_in_hours):
    load_dotenv()
    token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHANNEL_ID']

    if delay_in_hours is None:
        delay_in_hours = 4
    delay_in_seconds = float(delay_in_hours) * 3600
    filesindir = os.listdir(path=path)
    bot = telegram.Bot(token=token)
    while True:
        chosen_file = choice(filesindir)
        bot.send_document(
            chat_id=chat_id,
            document=open(f'{path}/{chosen_file}', 'rb')
            )
        filesindir.remove(chosen_file)
        if not filesindir:
            filesindir = os.listdir(path=path)
        time.sleep(delay_in_seconds)


def main():
    parser = argparse.ArgumentParser(
        description='Upload photo to Telegram channel with delay'
    )
    parser.add_argument(
        '-d', '--delay',
        help='set upload delay in hours. You can enter a floating point number'
        )
    args = parser.parse_args()
    delay = args.delay
    path = input('Enter the directory from which you want to publish photos:\n')
    publish_photo_by_tgbot(path, delay)


if __name__ == "__main__":
    main()
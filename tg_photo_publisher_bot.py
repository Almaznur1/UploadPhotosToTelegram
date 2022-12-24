import telegram
import os
from dotenv import load_dotenv
import argparse
from random import choice


def publish_photo(path, file, token, chat_id):
    filesindir = os.listdir(path=path)
    if file is None:
        file = choice(filesindir)
    bot = telegram.Bot(token=token)
    bot.send_document(
            chat_id=chat_id,
            document=open(f'{path}/{file}', 'rb')
            )


def main():
    load_dotenv()
    token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHANNEL_ID']
    parser = argparse.ArgumentParser(
        description='Upload photo to Telegram channel'
    )
    parser.add_argument(
        '-f', '--file',
        help='enter file name you want to publish'
        )
    args = parser.parse_args()
    file = args.file

    path = input('Enter the path from which you want to publish photo:\n')
    publish_photo(path, file, token, chat_id)


if __name__ == "__main__":
    main()

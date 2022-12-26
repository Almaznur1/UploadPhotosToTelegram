import telegram
import os
from dotenv import load_dotenv
import argparse
from random import choice


def publish_photo(path, token, chat_id):
    if not os.path.isabs(path):  # relative path case
        path = f'{os.path.dirname(os.path.abspath(__file__))}/{path}'

    if not os.path.isfile(path):
        path = f'{path}/{choice(os.listdir(path=path))}'

    bot = telegram.Bot(token=token)
    with open(path, 'rb') as file:
        bot.send_document(
            chat_id=chat_id,
            document=file
            )


def main():
    load_dotenv()
    token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHANNEL_ID']

    parser = argparse.ArgumentParser(
        description='Upload photo to Telegram channel'
    )
    parser.add_argument(
        'path',
        help='enter file or directory path you want to publish'
        )
    args = parser.parse_args()
    path = args.path

    publish_photo(path, token, chat_id)


if __name__ == "__main__":
    main()

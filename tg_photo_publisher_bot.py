import telegram
import os
from dotenv import load_dotenv
import argparse
from random import choice


def publish_photo(path, token, chat_id):
    if not os.path.isfile(path):
        path = f'{path}/{choice(os.listdir(path=path))}'
    bot = telegram.Bot(token=token)
    bot.send_document(
            chat_id=chat_id,
            document=open(path, 'rb')
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

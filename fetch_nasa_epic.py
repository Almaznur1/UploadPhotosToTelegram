import requests
import os
from dotenv import load_dotenv
from common_functions import make_save_dir
import argparse


def fetch_nasa_epic(token, save_dir):
    save_dir = make_save_dir(save_dir)

    url = 'https://api.nasa.gov/EPIC/api/natural/'
    params = {'api_key': token}
    response = requests.get(url, params=params)
    response.raise_for_status()

    photos = [
        (photo['image'], photo['date'])
        for photo in response.json()
        ]

    for index, photo in enumerate(photos, 1):
        filename = photo[0]
        date = photo[1][:10].replace('-', '/')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{filename}.png'
        response = requests.get(url, params=params)
        response.raise_for_status()
        filepath = f'{save_dir}/nasa_epic_{index}.png'
        with open(filepath, 'wb') as file:
            file.write(response.content)


def main():
    load_dotenv()
    token = os.environ['NASA_API_TOKEN']

    parser = argparse.ArgumentParser(
        description='Downloading NASA Earth photos')
    parser.add_argument('path', help='enter output directory path')
    args = parser.parse_args()
    output_dir = args.path

    fetch_nasa_epic(token, output_dir)


if __name__ == "__main__":
    main()

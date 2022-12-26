import requests
import os
from dotenv import load_dotenv
from common_functions import make_save_dir
import argparse


def fetch_nasa_epic(token, save_dir):
    save_dir = make_save_dir(save_dir)

    # getting data of photos
    url = 'https://api.nasa.gov/EPIC/api/natural/'
    params = {'api_key': token}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data_of_photos = []
    for photo in response.json():
        data_of_photos.append((photo['image'], photo['date']))

    # downloading photos
    for index, photo in enumerate(data_of_photos, 1):
        file = photo[0]
        date = photo[1][:10].replace('-', '/')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{file}.png'
        response = requests.get(url, params=params)
        response.raise_for_status()
        filename = f'{save_dir}/nasa_epic_{index}.png'
        with open(filename, 'wb') as file:
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

import requests
from pathlib import Path
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def fetch_spacex_last_launch(save_dir):
    if not os.path.isabs(save_dir):  # relative path case
        save_dir = f'{os.path.dirname(os.path.abspath(__file__))}/{save_dir}'
    Path(save_dir).mkdir(parents=True, exist_ok=True)

    # in the case there is no photos use this flight id: 5eb87d47ffd86e000604b38a
    response = requests.get('https://api.spacexdata.com/v5/launches/latest')
    response.raise_for_status()
    urls = response.json()['links']['flickr']['original']

    for index, url in enumerate(urls):
        response = requests.get(url)
        response.raise_for_status()
        filename = f'{save_dir}/spacex_{index}.jpg'
        with open(filename, 'wb') as file:
            file.write(response.content)


def get_nasa_apod(token, save_dir):
    if not os.path.isabs(save_dir):  # relative path case
        save_dir = f'{os.path.dirname(os.path.abspath(__file__))}/{save_dir}'
    Path(save_dir).mkdir(parents=True, exist_ok=True)

    url = 'https://api.nasa.gov/planetary/apod/'
    params = {'api_key': token, 'start_date': '2022-12-20', 'end_date': ''}
    response = requests.get(url, params=params)
    response.raise_for_status()
    urls = []
    for dict in response.json():
        urls.append(dict['url'])

    for index, url in enumerate(urls):
        if not get_file_ext(url):
            continue
        response = requests.get(url)
        response.raise_for_status()
        filename = f'{save_dir}/nasa_apod_{index}{get_file_ext(url)}'
        with open(filename, 'wb') as file:
            file.write(response.content)


def get_nasa_epic(token, save_dir):
    # creating save directory
    if not os.path.isabs(save_dir):  # relative path case
        save_dir = f'{os.path.dirname(os.path.abspath(__file__))}/{save_dir}'
    Path(save_dir).mkdir(parents=True, exist_ok=True)

    # getting data of photos
    url = 'https://api.nasa.gov/EPIC/api/natural/'
    params = {'api_key': token}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data_of_photos = []
    for photo in response.json():
        data_of_photos.append((photo['image'], photo['date']))

    # downloading photos
    for index, photo in enumerate(data_of_photos):
        file = photo[0]
        date = photo[1][:10].replace('-', '/')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{file}.png'
        response = requests.get(url, params=params)
        response.raise_for_status()
        filename = f'{save_dir}/nasa_epic_{index}.png'
        with open(filename, 'wb') as file:
            file.write(response.content)


def get_file_ext(url):
    url_parts = urlparse(url)
    file_ext = os.path.splitext(url_parts.path)
    return file_ext[1]


def main():
    load_dotenv()
    token = os.environ["NASA_API_TOKEN"]
    output_dir = input('Enter output path\n')
    # fetch_spacex_last_launch(output_dir)
    # get_nasa_apod(token, output_dir)
    get_nasa_epic(token, output_dir)


if __name__ == "__main__":
    main()

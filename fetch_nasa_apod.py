import requests
import os
from dotenv import load_dotenv
from common_functions import make_save_dir
from common_functions import get_file_ext
import argparse


def fetch_nasa_apod(token, save_dir):
    save_dir = make_save_dir(save_dir)

    url = 'https://api.nasa.gov/planetary/apod/'
    params = {'api_key': token, 'start_date': '2022-12-01', 'end_date': ''}
    response = requests.get(url, params=params)
    response.raise_for_status()

    urls = [dict['url'] for dict in response.json()]

    for index, url in enumerate(urls, 1):
        if not get_file_ext(url):              # skip all urls without files
            continue
        response = requests.get(url)
        response.raise_for_status()
        filename = f'{save_dir}/nasa_apod_{index}{get_file_ext(url)}'
        with open(filename, 'wb') as file:
            file.write(response.content)


def main():
    load_dotenv()
    token = os.environ['NASA_API_TOKEN']

    parser = argparse.ArgumentParser(
        description='Downloading NASA pictures')
    parser.add_argument('path', help='enter output directory path')
    args = parser.parse_args()
    output_dir = args.path

    fetch_nasa_apod(token, output_dir)


if __name__ == "__main__":
    main()

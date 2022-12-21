import requests
from pathlib import Path
import os
from dotenv import load_dotenv


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


def get_nasa_picture_of_the_day(token):
    url = 'https://api.nasa.gov/planetary/apod/'
    params = {'api_key': token}
    response = requests.get(url, params=params)
    response.raise_for_status()
    print(response.json()['url'])


def main():
    load_dotenv()
    # token = os.environ["NASA_API_TOKEN"]
    output_dir = input('Enter output path\n')
    fetch_spacex_last_launch(output_dir)
    # get_nasa_picture_of_the_day(token)


if __name__ == "__main__":
    main()

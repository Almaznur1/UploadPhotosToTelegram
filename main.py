import requests
from pathlib import Path
import os


def fetch_spacex_last_launch(save_dir):
    if not os.path.isabs(save_dir):  # relative path case
        save_dir = f'{os.path.dirname(os.path.abspath(__file__))}/{save_dir}'
    Path(save_dir).mkdir(parents=True, exist_ok=True)

    response = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
    response.raise_for_status()
    urls = response.json()['links']['flickr']['original'] 
    for index, url in enumerate(urls):
        response = requests.get(url)
        response.raise_for_status()
        filename = f'{save_dir}/spacex_{index}.jpg'
        with open(filename, 'wb') as file:
            file.write(response.content)


def main():
    output_dir = input('Enter output path\n')
    fetch_spacex_last_launch(output_dir)


if __name__ == "__main__":
    main()

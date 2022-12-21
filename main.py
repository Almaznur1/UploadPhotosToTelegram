import requests
from pathlib import Path
import os


def get_space_photo(url, output_dir):
    # absolute path case
    if os.path.isabs(output_dir):
        Path(f'{output_dir}').mkdir(parents=True, exist_ok=True)
        filename = f'{output_dir}/hubble.jpeg'
    # relative path case
    else:
        scripts_dir = os.path.dirname(os.path.abspath(__file__))
        Path(f'{scripts_dir}/{output_dir}').mkdir(parents=True, exist_ok=True)
        filename = f'{scripts_dir}/{output_dir}/hubble.jpeg'


    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def get_spacex_launch_photo_urs():
    response = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
    response.raise_for_status()

    space_launch_photo_urls = response.json()['links']['flickr']['original']
    for i in range(len(space_launch_photo_urls)):
        print(space_launch_photo_urls[i])


def main():
    url = ''  # input('Enter picture\'s URL\n')
    output_dir = input('Enter output path\n')
    get_space_photo(url, output_dir)
    get_spacex_launch_photo_urs()


if __name__ == "__main__":
    main()
 
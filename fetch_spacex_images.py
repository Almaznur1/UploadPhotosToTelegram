import requests
from common_functions import make_save_dir
import argparse


def fetch_spacex_last_launch(save_dir, id):
    save_dir = make_save_dir(save_dir)

    if id is None:
        id = 'latest'
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{id}')
    response.raise_for_status()
    if response.json()['links']['flickr']['original'] == []:
        print('There are no photos of this launch')
        return
    urls = response.json()['links']['flickr']['original']
    for index, url in enumerate(urls, 1):
        response = requests.get(url)
        response.raise_for_status()
        filename = f'{save_dir}/spacex_{index}.jpg'
        with open(filename, 'wb') as file:
            file.write(response.content)


def main():
    parser = argparse.ArgumentParser(
        description='Downloading spacex launch photo by id'
    )
    parser.add_argument(
        '-l', '--launch_id',
        help='enter launch id for downloading launch photos'
        )
    args = parser.parse_args()
    launch_id = args.launch_id

    output_dir = input('Enter output directory path:\n')
    fetch_spacex_last_launch(output_dir, launch_id)


if __name__ == "__main__":
    main()

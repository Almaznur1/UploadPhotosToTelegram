import requests
from pathlib import Path
import os


# def get_hubble_photo(save_dir):
#     if not os.path.isabs(save_dir):  # relative path case
#         save_dir = f'{os.path.dirname(os.path.abspath(__file__))}/{save_dir}'
#     Path(save_dir).mkdir(parents=True, exist_ok=True)
#     filename = f'{save_dir}/hubble.jpeg'

#     url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
#     response = requests.get(url)
#     response.raise_for_status()

#     with open(filename, 'wb') as file:
#         file.write(response.content)

def get_spacex_photo(urls, save_dir):
    if not os.path.isabs(save_dir):  # relative path case
        save_dir = f'{os.path.dirname(os.path.abspath(__file__))}/{save_dir}'
    Path(save_dir).mkdir(parents=True, exist_ok=True)

    for index, url in enumerate(urls):
        response = requests.get(url)
        response.raise_for_status()
        filename = f'{save_dir}/spacex_{index}.jpg'
        with open(filename, 'wb') as file:
            file.write(response.content)


def get_spacex_launch_photo_urs():
    response = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
    response.raise_for_status()
    photo_urls = response.json()['links']['flickr']['original'] 
    return (photo_urls)


def main():
    # Hubble photo getting 
    output_dir = input('Enter output path\n')
    # get_hubble_photo(output_dir)

    # SpaceX launch photo
    urls = get_spacex_launch_photo_urs()
    get_spacex_photo(urls, output_dir)


if __name__ == "__main__":
    main()

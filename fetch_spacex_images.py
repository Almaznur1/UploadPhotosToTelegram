import requests
from common_functions import mk_save_dir


def fetch_spacex_last_launch(save_dir):
    mk_save_dir(save_dir)

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

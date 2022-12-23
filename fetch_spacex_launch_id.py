import requests
import os


def fetch_spacex_launch_id():
    response = requests.get('https://api.spacexdata.com/v5/launches/')
    launches = response.json()
    filename = f'{os.path.dirname(os.path.abspath(__file__))}/spacex_id.txt'
    with open(filename, 'w') as file:
        for index, launch in enumerate(launches, 1):
            file.write(f'{index}. {launch["id"]}\n')


def main():
    fetch_spacex_launch_id()


if __name__ == "__main__":
    main()

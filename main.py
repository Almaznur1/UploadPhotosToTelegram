import requests
import pathlib
import os

scripts_dir = os.path.dirname(os.path.abspath(__file__))
pathlib.Path(f'{scripts_dir}/images').mkdir(parents=True, exist_ok=True)


filename = f'{scripts_dir}/images/hubble.jpeg'
url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'

response = requests.get(url)
response.raise_for_status()

with open(filename, 'wb') as file:
    file.write(response.content)

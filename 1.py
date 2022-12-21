import requests
import os
from dotenv import load_dotenv


load_dotenv()
token = os.environ["NASA_API_TOKEN"]
url = 'https://api.nasa.gov/planetary/apod/'
params = {'api_key': token}

response = requests.get(url, params=params)
print(response.json()['url'])
filename = 'picture_of_the_day.jpeg'
# with open(filename, 'wb') as file:
#     file.write(response.content)
#     print(file)

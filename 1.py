import requests


response = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
response.raise_for_status()

space_launch_photo_urls = response.json()['links']['flickr']['original']
for i in range(len(space_launch_photo_urls)):
    print(space_launch_photo_urls[i])

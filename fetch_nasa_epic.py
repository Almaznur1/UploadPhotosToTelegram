def get_nasa_epic(token, save_dir):
    # creating save directory
    if not os.path.isabs(save_dir):  # relative path case
        save_dir = f'{os.path.dirname(os.path.abspath(__file__))}/{save_dir}'
    Path(save_dir).mkdir(parents=True, exist_ok=True)

    # getting data of photos
    url = 'https://api.nasa.gov/EPIC/api/natural/'
    params = {'api_key': token}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data_of_photos = []
    for photo in response.json():
        data_of_photos.append((photo['image'], photo['date']))

    # downloading photos
    for index, photo in enumerate(data_of_photos):
        file = photo[0]
        date = photo[1][:10].replace('-', '/')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{file}.png'
        response = requests.get(url, params=params)
        response.raise_for_status()
        filename = f'{save_dir}/nasa_epic_{index}.png'
        with open(filename, 'wb') as file:
            file.write(response.content)
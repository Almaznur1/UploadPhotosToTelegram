def get_nasa_apod(token, save_dir):
    if not os.path.isabs(save_dir):  # relative path case
        save_dir = f'{os.path.dirname(os.path.abspath(__file__))}/{save_dir}'
    Path(save_dir).mkdir(parents=True, exist_ok=True)

    url = 'https://api.nasa.gov/planetary/apod/'
    params = {'api_key': token, 'start_date': '2022-12-20', 'end_date': ''}
    response = requests.get(url, params=params)
    response.raise_for_status()
    urls = []
    for dict in response.json():
        urls.append(dict['url'])

    for index, url in enumerate(urls):
        if not get_file_ext(url):
            continue
        response = requests.get(url)
        response.raise_for_status()
        filename = f'{save_dir}/nasa_apod_{index}{get_file_ext(url)}'
        with open(filename, 'wb') as file:
            file.write(response.content)
from pathlib import Path
import os
from urllib.parse import urlparse


def mk_save_dir(save_dir):
    if not os.path.isabs(save_dir):  # relative path case
        save_dir = f'{os.path.dirname(os.path.abspath(__file__))}/{save_dir}'
    Path(save_dir).mkdir(parents=True, exist_ok=True)


def get_file_ext(url):
    url_parts = urlparse(url)
    file_ext = os.path.splitext(url_parts.path)
    return file_ext[1]
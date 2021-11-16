import json
from pathlib import Path
from termcolor import cprint
from typing import Union, Any


def error_handler(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except BaseException as e:
            cprint(e, 'red', attrs=['bold'])
    return inner


def map_folder(path: Union[str, Path], ext: str = ''):
    return sorted(Path(path).rglob('*.{}'.format(ext)))


def save_data(path: Union[str, Path], data: Any):
    if Path(path).suffix == '.json':
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

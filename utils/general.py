from pathlib import Path
from typing import Union
from termcolor import cprint


def error_handler(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except BaseException as e:
            cprint(e, 'red', attrs=['bold'])
    return inner


def map_folder(path: Union[str, Path], ext: str = ''):
    return sorted(path.rglob('*.{}'.format(ext)))

import json
from PIL import Image
from pathlib import Path
from termcolor import cprint
from typing import Union, Any
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


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


def display(f: Union[str, Path], data: dict):
    plt.imshow(Image.open(f))
    x, y, w, h = data['x'], data['y'], data['w'], data['h']
    plt.gca().add_patch(Rectangle((x, y), w, h, linewidth=1, edgecolor='r', facecolor='none'))
    plt.show()

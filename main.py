from tqdm import tqdm
from pathlib import Path
from utils.handlers import MIO, ES
from utils.config import SRC_DIR, SRC_TYPE, DST_DIR, META_TYPE
from utils.general import error_handler, map_folder, save_data
from utils.config import MIO_HOST, MIO_SECRET_KEY, MIO_ACCESS_KEY, MIO_BUCKET, ES_HOST, ES_INDEX

mio_client = MIO(MIO_HOST, MIO_ACCESS_KEY, MIO_SECRET_KEY, MIO_BUCKET)
es_client = ES(ES_HOST, ES_INDEX)


@error_handler
def publisher():
    mio_client.create_bucket()
    for f in tqdm(map_folder(SRC_DIR, SRC_TYPE)):
        item = es_client.builder(f.stem)
        es_client.publisher(item)
        mio_client.upload_file(f)


@error_handler
def consumer():
    temp_dummy = {'x': 1, 'y': 1, 'w': 5, 'h': 5, 'cls': 'unknown'}
    Path(DST_DIR).mkdir(parents=True, exist_ok=True)
    for d in es_client.finder():
        mio_client.get_object(DST_DIR, '{}.{}'.format(d['_source']['entity_id'], SRC_TYPE))
        save_data('{}/{}.{}'.format(DST_DIR, d['_source']['entity_id'], META_TYPE), temp_dummy)


if __name__ == '__main__':
    publisher()

from tqdm import tqdm
from utils.handlers import MIO, ES
from utils.config import SRC_DIR, SRC_TYPE
from utils.general import error_handler, map_folder
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
    for d in es_client.finder():
        print('{}.{}'.format(d['_source']['entity_id'], SRC_TYPE))


if __name__ == '__main__':
    consumer()

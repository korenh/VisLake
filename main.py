from pathlib import Path
from utils.handlers import MIO, ES, Static, error_handler
from utils.config import SRC_DIR, VIS_TYPE, DST_DIR,  MIO_VISUAL_BUCKET, ES_HOST, META_TYPE
from utils.config import MIO_HOST, MIO_SECRET_KEY, MIO_ACCESS_KEY, MIO_META_BUCKET, ES_INDEX

es_client = ES(ES_HOST)
mio_client = MIO(MIO_HOST, MIO_ACCESS_KEY, MIO_SECRET_KEY)


@error_handler
def publisher():
    mio_client.create_bucket(MIO_META_BUCKET)
    mio_client.create_bucket(MIO_VISUAL_BUCKET)
    np_l, im_l = Static.map_folder(SRC_DIR, META_TYPE), Static.map_folder(SRC_DIR, VIS_TYPE)
    for np_l, im_l in zip(np_l, im_l):
        item = es_client.builder({'entity_id': np_l.stem})
        es_client.publisher(item, ES_INDEX)
        mio_client.upload_file(im_l, MIO_VISUAL_BUCKET)
        mio_client.upload_file(np_l, MIO_META_BUCKET)


@error_handler
def consumer():
    Path(DST_DIR).mkdir(parents=True, exist_ok=True)
    for d in es_client.finder(ES_INDEX):
        mio_client.get_file(DST_DIR, '{}.{}'.format(Path(d['_source']['entity_id']).stem, VIS_TYPE), MIO_VISUAL_BUCKET)
        mio_client.get_file(DST_DIR, '{}.{}'.format(Path(d['_source']['entity_id']).stem, META_TYPE), MIO_META_BUCKET)


if __name__ == '__main__':
    consumer()



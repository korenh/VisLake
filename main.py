import pandas as pd
from tqdm import tqdm
from pathlib import Path
from utils.handlers import MIO, ES
from utils.config import SRC_DIR, SRC_TYPE, DST_DIR, META_TYPE
from utils.general import error_handler, display, save_data
from utils.config import MIO_HOST, MIO_SECRET_KEY, MIO_ACCESS_KEY, MIO_BUCKET, ES_HOST, ES_INDEX

mio_client = MIO(MIO_HOST, MIO_ACCESS_KEY, MIO_SECRET_KEY, MIO_BUCKET)
es_client = ES(ES_HOST, ES_INDEX)


@error_handler
def publisher():
    mio_client.create_bucket()
    df = pd.read_csv('data/dataset/train_solution_bounding_boxes (1).csv')
    for index, row in tqdm(df.iterrows()):
        item = es_client.builder(row)
        es_client.publisher(item)
        mio_client.upload_file(Path('{}/{}'.format(SRC_DIR, row['image'])))


@error_handler
def consumer():
    Path(DST_DIR).mkdir(parents=True, exist_ok=True)
    for d in es_client.finder():
        mio_client.get_object(DST_DIR, '{}.{}'.format(Path(d['_source']['entity_id']).stem, SRC_TYPE))
        data = {'x': d['_source']['y'], 'y': d['_source']['y'], 'w': d['_source']['w'], 'h': d['_source']['h']}
        save_data('{}/{}.{}'.format(DST_DIR, Path(d['_source']['entity_id']).stem, META_TYPE), data)
        display('{}/{}.{}'.format(DST_DIR, Path(d['_source']['entity_id']).stem, SRC_TYPE), data)


if __name__ == '__main__':
    pass



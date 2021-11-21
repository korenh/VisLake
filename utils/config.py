import os

SRC_DIR = os.getenv('SRC_DIR', './data/dataset/training_images')
DST_DIR = os.getenv('DST_DIR', './data/output')
SRC_TYPE = os.getenv('SRC_TYPE', 'jpg')
META_TYPE = os.getenv('META_TYPE', 'json')

ES_HOST = os.getenv('ES_HOST', 'localhost')
ES_PORT = int(os.getenv('ES_PORT', 9200))
ES_USERNAME = os.getenv('ES_USERNAME', 'elastic')
ES_PASSWORD = os.getenv('ES_PASSWORD', 'secret')
ES_INDEX = os.getenv('ES_INDEX', 'test')

MIO_HOST = os.getenv('MIO_HOST', 'localhost:9000')
MIO_ACCESS_KEY = os.getenv('MIO_ACCESS_KEY', 'minioadmin')
MIO_SECRET_KEY = os.getenv('MIO_SECRET_KEY', 'minioadmin')
MIO_BUCKET = os.getenv('MIO_BUCKET', 'test')


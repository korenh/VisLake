import os

SRC_DIR = os.getenv('SRC_DIR', './data/')
SRC_TYPE = os.getenv('SRC_TYPE', 'shp')

ES_HOST = os.getenv('ES_HOST', 'localhost')
ES_PORT = int(os.getenv('ES_PORT', 9200))
ES_USERNAME = os.getenv('ES_USERNAME', 'elastic')
ES_PASSWORD = os.getenv('ES_PASSWORD', 'secret')
ES_INDEX = os.getenv('ES_INDEX', 'test')

MIO_HOST = os.getenv('localhost:9000')
MIO_ACCESS_KEY = os.getenv('MIO_ACCESS_KEY', 'minioadmin')
MIO_SECRET_KEY = os.getenv('MIO_SECRET_KEY', 'minioadmin')
MIO_BUCKET = os.getenv('MIO_BUCKET', 'test')


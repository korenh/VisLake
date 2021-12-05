from minio import Minio
from pathlib import Path
from termcolor import cprint
from datetime import datetime
from typing import Union, Dict
from elasticsearch import Elasticsearch


class MIO:
    def __init__(self, url: str, access_key: str, secret_key: str, secure: bool = False):
        self.client = Minio(url, access_key=access_key, secret_key=secret_key, secure=secure)

    def create_bucket(self, bucket: str):
        if not self.client.bucket_exists(bucket):
            self.client.make_bucket(bucket)

    def upload_file(self, path: Union[str, Path], bucket: str):
        return self.client.fput_object(bucket, '{}{}'.format(path.stem, path.suffix), path)

    def get_file(self, dst: Union[str, Path], object_name: str, bucket: str):
        return self.client.fget_object(bucket, object_name, '{}/{}'.format(dst, object_name))


class ES:
    def __init__(self, host: str):
        self.client = Elasticsearch([host])

    def publisher(self, item: Dict, index: str):
        return self.client.index(index=index, body=item)

    def finder(self, index: str):
        query = {"size": 100, "query": {"query_string": {"query": "*", "fields": ["entity_id"]}}}
        return self.client.search(index=index, body=query)['hits']['hits']

    @staticmethod
    def builder(data):
        return {'entity_id': data['entity_id'],
                'timestamp': datetime.utcnow()}


class Static:
    @staticmethod
    def map_folder(path: Union[str, Path], ext: str = ''):
        return sorted(Path(path).rglob('*.{}'.format(ext)))


def error_handler(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except BaseException as e:
            cprint(e, 'red', attrs=['bold'])
    return inner

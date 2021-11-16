from minio import Minio
from pathlib import Path
from datetime import datetime
from typing import Union, Dict
from elasticsearch import Elasticsearch


class MIO:
    def __init__(self, url: str, access_key: str, secret_key: str, bucket: str, secure: bool = False):
        self.client = Minio(url, access_key=access_key, secret_key=secret_key, secure=secure)
        self.bucket = bucket

    def create_bucket(self):
        if not self.client.bucket_exists(self.bucket):
            self.client.make_bucket(self.bucket)

    def remove_bucket(self):
        self.client.remove_bucket(self.bucket)

    def upload_file(self, path: Union[str, Path]):
        return self.client.fput_object(self.bucket, '{}{}'.format(path.stem, path.suffix), path)

    def get_object(self, dst: Union[str, Path], object_name: str):
        return self.client.fget_object(self.bucket, object_name, '{}/{}'.format(dst, object_name))


class ES:
    def __init__(self, host: str, index: str):
        self.client = Elasticsearch([host])
        self.index = index

    def publisher(self, item: Dict):
        return self.client.index(index=self.index, body=item)

    def finder(self):
        query = {"size": 50, "query": {"query_string": {"query": "*", "fields": ["entity_id"]}}} # sample query
        return self.client.search(index=self.index, body=query)['hits']['hits']

    @staticmethod
    def builder(data):
        return {'entity_id': data,
                'meta': {},
                'timestamp': datetime.utcnow()}

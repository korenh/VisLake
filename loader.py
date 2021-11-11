from utils.handlers import MIO, ES
from utils.general import error_handler
from utils.config import MIO_HOST, MIO_SECRET_KEY, MIO_ACCESS_KEY, MIO_BUCKET, ES_HOST, ES_INDEX


@error_handler
def main():
    mio_client = MIO(MIO_HOST, MIO_ACCESS_KEY, MIO_SECRET_KEY, MIO_BUCKET)
    es_client = ES(ES_HOST, ES_INDEX)


if __name__ == '__main__':
    main()

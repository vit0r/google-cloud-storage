#!/usr/bin/env python3

from os import sys, environ
from google.cloud import storage

assert 'GOOGLE_APPLICATION_CREDENTIALS' in environ, 'GOOGLE_APPLICATION_CREDENTIALS unset'
storage_client = storage.Client()
bucket_name, *_ = sys.argv
bucket = storage_client.get_bucket(bucket_name)
print('Bucket {}.'.format(bucket.name))

"""
s3-download-and-delete

Usage: go.py --bucket=<bucket> --directory=<directory>

Options:
 --bucket=<bucket>              The name of the S3 bucket to download stuff off and clear out
 --directory=<directory>        The directory to download the files to
"""

import boto3
from docopt import docopt
import os

client = boto3.client('s3')

def get_contents(bucket, directory):
  contents = []
  paginator = client.get_paginator('list_objects_v2')
  page_iterator = paginator.paginate(Bucket=bucket)

  for page in page_iterator:
    contents = contents + page['Contents']

  for content in contents:
    client.download_file(bucket, content['Key'], os.path.join(os.getcwd(), directory, content['Key']))

  client.delete_objects(Bucket=bucket, Delete={
    'Objects': map(lambda x: {'Key': x['Key']}, contents)
  })

if __name__ == '__main__':
  options = docopt(__doc__)
  get_contents(options['--bucket'], options['--directory'])

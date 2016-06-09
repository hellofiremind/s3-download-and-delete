"""
s3-download-and-delete

Usage:
  python go.py --bucket foo --directory .

Options:
 --bucket           The name of the S3 bucket to download stuff off and clear out
 --directory        The directory to download the files to

Examples:
  python go.py --bucket foo --directory .

Help:
  Visit https://github.com/wearescouting/s3-download-and-delete
"""

import boto3
import docopt
import os
import sys

client = boto3.client('s3')

def get_contents():
  contents = []
  paginator = client.get_paginator('list_objects_v2')
  page_iterator = paginator.paginate(Bucket=os.getenv('BUCKET'))

  for page in page_iterator:
    contents = contents + page['Contents']

  for content in contents:
    client.download_file(os.getenv('BUCKET'), content['Key'], os.getenv('DIRECTORY') + '/' + content['Key'])

  client.delete_objects(Bucket=os.getenv('BUCKET'), Delete={
    'Objects': map(lambda x: {'Key': x['Key']}, contents)
  })

get_contents()
# def main():
#   options = docopt(__doc__, version='1.0.0')

#   for k, v in options.iteritems():


# main()

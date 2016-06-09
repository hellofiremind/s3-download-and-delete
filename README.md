# S3 download and delete
A simple python script that downloads and deletes files from an S3 bucket

## Usage

```
AWS_ACCESS_KEY_ID=KEY AWS_SECRET_ACCESS_KEY=SECRET python go.py --bucket=BUCKET --directory=RELATIVE_PATH
```

If you get an error like: "The bucket you are attempting to access must be addressed using the specified endpoint. Please send all future requests to this endpoint"; then simply added the bucket's region in the envrionment variable `AWS_DEFAULT_REGION`, eg `AWS_DEFAULT_REGION=eu-west-1`

#!/usr/bin/env python3
import boto3
import urllib.request
import argparse
import sys

def fetch_file(source_url, dest_file):
    try:
        urllib.request.urlretrieve(source_url, dest_file)
        print(f"successfully fetched file from {source_url} as {dest_file}")
    except Exception as error:
        print(f"error fetching file: {error}")
        sys.exit(1)

def s3_upload(client, bucket, file_path, s3_key, access="private"):
    try:
        client.upload_file(file_path, bucket, s3_key, ExtraArgs={'ACL': access})
        print(f"uploaded {file_path} to s3://{bucket}/{s3_key} with acl='{access}'")
    except Exception as error:
        print(f"error during s3 upload: {error}")
        sys.exit(1)

def create_presigned_url(client, bucket, s3_key, validity_seconds):
    try:
        presigned = client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket, 'Key': s3_key},
            ExpiresIn=validity_seconds
        )
        return presigned
    except Exception as error:
        print(f"error generating presigned url: {error}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_url')
    parser.add_argument('s3_bucket')
    parser.add_argument('--validity', type=int, default=604800)
    parser.add_argument('--s3key', dest='object_key', default=None)
    args = parser.parse_args()
    local_fname = args.file_url.split("/")[-1]
    s3_object = args.object_key if args.object_key else local_fname
    s3_client = boto3.client('s3', region_name='us-east-1')
    fetch_file(args.file_url, local_fname)
    s3_upload(s3_client, args.s3_bucket, local_fname, s3_object, access="private")
    url = create_presigned_url(s3_client, args.s3_bucket, s3_object, args.validity)
    print(f"\ngenerated presigned url (valid for {args.validity} seconds):\n{url}")

if __name__ == '__main__':
    main()


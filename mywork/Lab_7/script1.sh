
#!/bin/bash
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <local_filename> <bucket_name> <expiration_seconds>"
    exit 1
fi

FILE_PATH=$1
BUCKET_ID=$2
EXPIRE_TIME=$3

if [ ! -f "$FILE_PATH" ]; then
    echo "error: file '$FILE_PATH' not found."
    exit 1
fi

echo "uploading $FILE_PATH to s3://$BUCKET_ID/ ..."
aws s3 cp "$FILE_PATH" s3://"$BUCKET_ID"/

if [ $? -ne 0 ]; then
    echo "file failed to upload"
    exit 1
fi

echo "file uploaded successfully"
echo "generating a presigned URL (expires in $EXPIRE_TIME seconds)"

SIGNED_URL=$(aws s3 presign --expires-in "$EXPIRE_TIME" s3://"$BUCKET_ID"/$(basename "$FILE_PATH"))
echo "Presigned URL: $SIGNED_URL"

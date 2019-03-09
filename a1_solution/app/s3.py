import boto3
# Let's use Amazon S3
s3 = boto3.resource('s3')

# Boto 3
import boto3
s3 = boto3.resource('s3')
s3.create_bucket(Bucket='mybucket')
s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={
    'LocationConstraint': 'us-east-1'})
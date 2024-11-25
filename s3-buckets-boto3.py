# pip install boto3
# aws configure

import boto3
import os

# Create and Manage S3 Buckets using Boto3
# variables
s3 = boto3.client('s3')
bucket_name = "my-awsclass-demo-bucket-boto3"
file_name = "example.txt"
download_file_name = "downloaded_example.txt"

# Create an S3 bucket.
def create_bucket(bucket_name):
    """Create an S3 bucket."""
    try:
        s3.create_bucket(
            Bucket=bucket_name,
        )
        print(f"Bucket '{bucket_name}' created successfully!")
    except Exception as e:
        print(f"Error creating bucket: {e}")
# Upload a file to the bucket.
def upload_file(bucket_name, file_name):
    """Upload a file to the S3 bucket."""
    with open(file_name, "w") as f:
        f.write("This is a demo file for the Boto3 exercise.")
    
    try:
        s3.upload_file(file_name, bucket_name, file_name)
        print(f"File '{file_name}' uploaded successfully to bucket '{bucket_name}'!")
    except Exception as e:
        print(f"Error uploading file: {e}")
# List all files in the bucket.
def list_files(bucket_name):
    """List all files in the S3 bucket."""
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            print("Files in bucket:")
            for obj in response['Contents']:
                print(f" - {obj['Key']}")
        else:
            print("No files found in bucket.")
    except Exception as e:
        print(f"Error listing files: {e}")
# Delete a file from the bucket.
def delete_file(bucket_name, file_name):
    """Delete a file from the S3 bucket."""
    try:
        s3.delete_object(Bucket=bucket_name, Key=file_name)
        print(f"File '{file_name}' deleted successfully from bucket '{bucket_name}'!")
    except Exception as e:
        print(f"Error deleting file: {e}")
# Delete the bucket.
def delete_bucket(bucket_name):
    """Delete an S3 bucket."""
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully!")
    except Exception as e:
        print(f"Error deleting bucket: {e}")
# Workflow execution
if __name__ == "__main__":
    create_bucket(bucket_name)
    upload_file(bucket_name, file_name)
    list_files(bucket_name)
    delete_file(bucket_name, file_name)
    delete_bucket(bucket_name)
    
# Challenges :
# Handle exceptions when creating a bucket with a name that already exists.
# Use environment variables for AWS credentials.

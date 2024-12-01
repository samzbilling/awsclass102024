import boto3
import os

# Initialize AWS clients
s3 = boto3.client('s3')

# Variables
bucket_name = "my-file-processing-bucket-py"
athena_results_bucket = "my-athena-query-results-py"

# S3: Create a Bucket
def create_s3_bucket(bucket_name):
    """Create an S3 bucket."""
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f"S3 bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error creating S3 bucket: {e}")

def setup_athena_query_results_bucket(athena_results_bucket):
    """Set up an S3 bucket for Athena query results."""
    create_s3_bucket(athena_results_bucket)
    print(f"S3 bucket '{athena_results_bucket}' is ready for Athena query results.")

def extract_s3_event(event):
    """Parse S3 event to get bucket and file details."""
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    return bucket_name, file_name

def fetch_s3_metadata(bucket_name, file_name):
    """Fetch metadata of a file from S3."""
    try:
        response = s3.head_object(Bucket=bucket_name, Key=file_name)
        metadata = {
            "FileName": file_name,
            "BucketName": bucket_name,
            "ContentType": response.get('ContentType'),
            "FileSize": response.get('ContentLength'),
            "LastModified": str(response.get('LastModified'))
        }
        print(f"Fetched metadata for file: {file_name}")
        return metadata
    except Exception as e:
        print(f"Error fetching S3 metadata: {e}")
        return None
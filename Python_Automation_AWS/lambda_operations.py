import boto3
import json

lambda_client = boto3.client('lambda')
iam_client = boto3.client('iam')

def create_lambda_function(function_name, role_arn, bucket_name, handler_name, zip_file_path):
    """Create or update a Lambda function."""
    try:
        with open(zip_file_path, 'rb') as f:
            zip_file_bytes = f.read()

        # Create or update Lambda function
        try:
            response = lambda_client.create_function(
                FunctionName=function_name,
                Runtime='python3.9',
                Role=role_arn,
                Handler=handler_name,
                Code={'ZipFile': zip_file_bytes},
                Description="Lambda function for S3 file processing",
                Timeout=30,
                MemorySize=128,
            )
            print(f"Lambda function '{function_name}' created successfully.")
        except lambda_client.exceptions.ResourceConflictException:
            response = lambda_client.update_function_code(
                FunctionName=function_name,
                ZipFile=zip_file_bytes,
            )
            print(f"Lambda function '{function_name}' updated successfully.")
    except Exception as e:
        print(f"Error creating/updating Lambda function: {e}")


def create_s3_trigger(bucket_name, function_name):
    """Add S3 trigger to Lambda function."""
    try:
        s3 = boto3.client('s3')
        response = s3.put_bucket_notification_configuration(
            Bucket=bucket_name,
            NotificationConfiguration={
                'LambdaFunctionConfigurations': [
                    {
                        'LambdaFunctionArn': lambda_client.get_function(FunctionName=function_name)['Configuration']['FunctionArn'],
                        'Events': ['s3:ObjectCreated:*']
                    }
                ]
            }
        )
        print(f"S3 trigger added for bucket '{bucket_name}' and Lambda function '{function_name}'.")
    except Exception as e:
        print(f"Error creating S3 trigger: {e}")

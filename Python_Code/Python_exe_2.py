
# Boto3 Documentation

# https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

# Exercise 1: Create and Manage S3 Buckets with Boto3 library.
# Objective: Teach students how to interact with Amazon S3 using Boto3 library.This includes:
    # Creating and managing S3 buckets.
    # Uploading files to and deleting files from an S3 bucket.
    # Handling exceptions when interacting with S3.
    # Using environment variables for AWS credentials to keep the credentials secure.
    
# Steps:
    # Setup AWS credentials using environment variables.
    # Create an S3 bucket and handle the exception if the bucket name already exists.
    # Upload a file to the bucket.
    # List all files in the bucket.
    # Delete a file from the bucket.
    # Delete the S3 bucket.

# Challenges:
    # Handle exceptions when creating a bucket with a name that already exists.
    # Use environment variables for AWS credentials.

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
import os

# Initialize the S3 client
s3_client = boto3.client('s3')

# 1. Create an S3 bucket
def create_s3_bucket(bucket_name):
    try:
        # Create the bucket
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' created successfully.")
    except s3_client.exceptions.BucketAlreadyExists as e:
        print(f"Bucket name '{bucket_name}' already exists. Try another unique name.")
    except s3_client.exceptions.BucketAlreadyOwnedByYou as e:
        print(f"Bucket '{bucket_name}' is already owned by your AWS account.")
    except NoCredentialsError:
        print("Credentials not available.")
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
    except ClientError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unknown error occurred: {e}")

# 2. Upload a file to the bucket
def upload_file_to_s3(bucket_name, file_path, object_name):
    try:
        # Upload the file
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' uploaded to '{bucket_name}/{object_name}' successfully.")
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except NoCredentialsError:
        print("Credentials not available.")
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
    except ClientError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unknown error occurred: {e}")

# 3. List all files in the bucket
def list_files_in_s3(bucket_name):
    try:
        # List objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            print(f"Files in '{bucket_name}':")
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print(f"No files found in '{bucket_name}'.")
    except NoCredentialsError:
        print("Credentials not available.")
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
    except ClientError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unknown error occurred: {e}")

# 4. Delete a file from the bucket
def delete_file_from_s3(bucket_name, object_name):
    try:
        # Delete the file
        s3_client.delete_object(Bucket=bucket_name, Key=object_name)
        print(f"File '{object_name}' deleted from '{bucket_name}' successfully.")
    except NoCredentialsError:
        print("Credentials not available.")
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
    except ClientError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unknown error occurred: {e}")

# 5. Delete the bucket
def delete_s3_bucket(bucket_name):
    try:
        # Delete the bucket
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted successfully.")
    except NoCredentialsError:
        print("Credentials not available.")
    except PartialCredentialsError:
        print("Incomplete credentials provided.")
    except ClientError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unknown error occurred: {e}")


# Example usage:

if __name__ == "__main__":
    # Set the bucket name, file path, and object name
    bucket_name = "shopsmartlytoday-bucket"  # Must be unique globally
    file_path = r"C:\Repositories\awsclass102024\Python_Code\sample.txt"  
    object_name = "uploaded_file.txt"  # S3 object name for the file

    # Check if the file exists locally, if not, create it
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("This is a sample file content.")
        print(f"File '{file_path}' created.")

    # 1. Create the bucket
    create_s3_bucket(bucket_name)

    # 2. Upload the file to the bucket
    upload_file_to_s3(bucket_name, file_path, object_name)

    # 3. List files in the bucket
    list_files_in_s3(bucket_name)

    # 4. Delete the file from the bucket
    delete_file_from_s3(bucket_name, object_name)

    # 5. List files again to ensure the file was deleted
    list_files_in_s3(bucket_name)

    # 6. Delete the bucket
    delete_s3_bucket(bucket_name)





# Exercise 2: DynamoDB CRUD Operations
# Objective: Teach students how to interact with DynamoDB using Boto3.

# Steps:

# Create a DynamoDB table (e.g., Students with attributes StudentID and Name).
# Insert records into the table.
# Retrieve all records.
# Update a record in the table.
# Delete a record from the table.
# Challenges :

# Use the correct data types for attributes (e.g., string, number).
# Implement a function to query the table based on a specific StudentID.

# Exercise 3: EC2 Instance Management
# Objective: Teach students how to launch and manage EC2 instances using Boto3.

# Steps:

# Launch an EC2 instance.
# Retrieve the public IP address of the instance.
# Stop the instance.
# Start the instance again.
# Terminate the instance.
# Challenges :

# Use tags to name the instance.
# Create a security group and associate it with the instance.
# Handle errors when attempting to start/stop an already running/stopped instance.

# Exercise 4: Lambda Function Deployment
# Objective: Teach students how to deploy and invoke an AWS Lambda function using Boto3.

# Steps:

# Create a Lambda function using an existing zip file.
# Add an execution role to the Lambda function.
# Invoke the Lambda function and display the response.
# Update the Lambda function code.
# Delete the Lambda function.
# Challenges :

# Use IAM to create a role programmatically for Lambda.
# Handle versioning when updating the function.

# Exercise 5: CloudWatch Logs and Monitoring
# Objective: Teach students how to use CloudWatch for logging and monitoring resources.

# Steps:

# Create a log group and log stream.
# Write a custom log entry to the stream.
# Retrieve log events from the stream.
# Set up a metric filter on the log group.
# Delete the log group.
# Challenges :

# Create and use IAM policies that allow access to CloudWatch.
# Parse log data to find specific patterns (e.g., errors or warnings).

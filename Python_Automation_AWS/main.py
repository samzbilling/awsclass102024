# pip install boto3
# aws configure

from s3_operations import create_s3_bucket,setup_athena_query_results_bucket, extract_s3_event, fetch_s3_metadata
from dynamodb_operations import create_dynamodb_table, insert_metadata_into_dynamodb
from sns_operations import create_sns_topic, send_sns_notification
from ses_operations import verify_ses_email, send_ses_email
from lambda_operations import create_lambda_function, create_s3_trigger
from athena_operations import create_athena_database, create_metadata_table, execute_query, wait_for_query_to_complete, get_query_results

# Variables
bucket_name = "my-file-processing-bucket-py"
table_name = "FileMetadataTable"
sns_topic_name = "FileUploadNotifications"
sender_email = "tsegazeabmulugeta@gmail.com"
recipient_email = "tsegazeabmberhie@gmail.com"
lambda_function_name = "S3FileProcessorLambda"
lambda_role_arn = "arn:aws:iam::359533991697:role/Python_automation_project"
lambda_handler_name = "lambda_function.lambda_handler"
zip_file_path = "lambda_function.zip" # Path to the zipped Lambda function code
athena_database = "s3_metadata_db"
athena_table = "s3_file_metadata"
s3_metadata_location = "s3://my-file-processing-bucket-py/"
athena_output_location = "s3://my-athena-query-results-py/"


if __name__ == "__main__":
    # S3: Create bucket
    create_s3_bucket(bucket_name)

    # Athena: Create the Athena query results bucket
    setup_athena_query_results_bucket("my-athena-query-results-py")

    # DynamoDB: Create table
    table = create_dynamodb_table(table_name)
    if not table:
        print("DynamoDB table creation failed.")
        exit()

    # Example metadata
    metadata = {
        "FileName": "example.txt",
        "BucketName": bucket_name,
        "ContentType": "text/plain",
        "FileSize": 1024,
        "LastModified": "2024-11-30T12:34:56Z"
    }

    # DynamoDB: Insert metadata
    insert_metadata_into_dynamodb(table, metadata)

    # SNS: Create topic and send notification
    topic_arn = create_sns_topic(sns_topic_name)
    if topic_arn:
        send_sns_notification(topic_arn, f"File '{metadata['FileName']}' uploaded to bucket '{bucket_name}'.")

    # SES: Verify and send email
    verify_ses_email(sender_email)
    verify_ses_email(recipient_email)
    send_ses_email(
        sender_email,
        recipient_email,
        f"File Uploaded: {metadata['FileName']}",
        f"Metadata: {metadata}"
    )

    # Lambda: Create Lambda function
    create_lambda_function(
        function_name=lambda_function_name,
        role_arn=lambda_role_arn,
        bucket_name=bucket_name,
        handler_name=lambda_handler_name,
        zip_file_path=zip_file_path
    )

    # Add S3 trigger for Lambda function
    create_s3_trigger(bucket_name, lambda_function_name)

    # Example query: List all files in S3 metadata table
    query = "SELECT FileName, ContentType, FileSize, LastModified FROM s3_file_metadata;"
    
    # Athena: Execute Athena query
    create_athena_database(athena_database, athena_output_location)

    # Step 2: Create Athena table linked to S3 metadata
    create_metadata_table(
        database_name=athena_database,
        table_name=athena_table,
        s3_location=s3_metadata_location,
        output_location=athena_output_location
    )

    # Step 3: Execute a query and fetch results
    query = "SELECT FileName, ContentType, FileSize, LastModified FROM s3_file_metadata;"
    query_execution_id = execute_query(athena_database, query, athena_output_location)
    
    if query_execution_id:
        # Wait for the query to complete
        state = wait_for_query_to_complete(query_execution_id)
        if state == "SUCCEEDED":
            # Fetch and print query results
            results = get_query_results(query_execution_id)
            print("Query Results:")
            for row in results:
                print(row)
        else:
            print(f"Query failed with state: {state}")
    else:
        print("Failed to start query.")

    print("Athena setup and query execution completed successfully.")
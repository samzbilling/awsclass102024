import boto3

dynamodb = boto3.resource('dynamodb')

def create_dynamodb_table(table_name):
    """Create a DynamoDB table for metadata."""
    try:
        existing_table = dynamodb.Table(table_name)
        existing_table.load()
        print(f"DynamoDB table '{table_name}' already exists.")
        return existing_table
    except dynamodb.meta.client.exceptions.ResourceNotFoundException:
        try:
            table = dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {"AttributeName": "FileName", "KeyType": "HASH"},
                ],
                AttributeDefinitions=[
                    {"AttributeName": "FileName", "AttributeType": "S"},
                ],
                ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
            )
            table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
            print(f"DynamoDB table '{table_name}' created successfully.")
            return table
        except Exception as e:
            print(f"Error creating DynamoDB table: {e}")
            return None

def insert_metadata_into_dynamodb(table, metadata):
    """Insert metadata into the DynamoDB table."""
    try:
        table.put_item(
            Item={
                "FileName": metadata["FileName"],
                "BucketName": metadata["BucketName"],
                "ContentType": metadata["ContentType"],
                "FileSize": metadata["FileSize"],
                "LastModified": metadata["LastModified"],
            }
        )
        print(f"Metadata for file '{metadata['FileName']}' inserted successfully.")
    except Exception as e:
        print(f"Error inserting metadata: {e}")

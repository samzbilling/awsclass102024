# pip install boto3
# aws configure

import boto3
import os

# DynamoDB CRUD Operations using Boto3
# variables
dynamodb = boto3.resource('dynamodb')
table_name = "My-dynamodb-table-with-boto3"
# Create a DynamoDB table and insert records into the table. (e.g., Students with attributes StudentID and Name).
def create_dynamodb(table_name):
    """Create a dynamo-db table"""
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
    # Wait until the table exists.
    table.wait_until_exists()

    # Print out some data about the table.
    print(table.item_count)

    table = dynamodb.Table(table_name)  # Get the table object
    table.put_item(
        Item={
            'username': 'janedoe',
            'first_name': 'Jane',
            'last_name': 'Doe',
            'age': 25,
            'account_type': 'standard_user',
        }
    )
    print(f"Table '{table_name}' created successfully!")


# Retrieve all records.
def retrieve_record(table_name):
    table = dynamodb.Table(table_name)
    response = table.get_item(
        Key={
            'username': 'janedoe',
            'last_name': 'Doe'
        }
    )
    item = response['Item']
    print("Retrieved item:", item)
    print(item)


# Update a record in the table.
def update_record(table_name):
    table = dynamodb.Table(table_name)
    table.update_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 27
    }
    )
    print("Updated a record")
# Delete a record from the table.
def delete_record(table_name):
    table = dynamodb.Table(table_name)
    table.delete_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    },    
    )
    print("Deleted a record")
# Workflow execution
if __name__ == "__main__":
    create_dynamodb(table_name)
    retrieve_record(table_name)
    update_record(table_name)
    delete_record(table_name)

# Challenges:
# Use the correct data types for attributes (e.g., string, number).
# Implement a function to query the table based on a specific StudentID.
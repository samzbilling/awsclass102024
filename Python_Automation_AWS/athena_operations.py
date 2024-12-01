import boto3
import time

# Initialize Athena client
athena_client = boto3.client('athena')

def execute_query(database, query, output_location):
    """Run an Athena query and return the QueryExecutionId."""
    try:
        response = athena_client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={"Database": database},
            ResultConfiguration={"OutputLocation": output_location}
        )
        query_execution_id = response["QueryExecutionId"]
        print(f"Query started: {query_execution_id}")
        return query_execution_id
    except Exception as e:
        print(f"Error starting query: {e}")
        return None

def wait_for_query_to_complete(query_execution_id):
    """Wait for the Athena query to complete."""
    try:
        while True:
            response = athena_client.get_query_execution(QueryExecutionId=query_execution_id)
            state = response["QueryExecution"]["Status"]["State"]
            if state in ["SUCCEEDED", "FAILED", "CANCELLED"]:
                return state
            time.sleep(1)
    except Exception as e:
        print(f"Error waiting for query to complete: {e}")
        return None

def get_query_results(query_execution_id):
    """Fetch results from a completed Athena query."""
    try:
        results = []
        paginator = athena_client.get_paginator('get_query_results')
        for page in paginator.paginate(QueryExecutionId=query_execution_id):
            for row in page["ResultSet"]["Rows"]:
                results.append(row)
        return results
    except Exception as e:
        print(f"Error fetching query results: {e}")
        return None

def create_athena_database(database_name, output_location):
    """Create an Athena database."""
    query = f"CREATE DATABASE IF NOT EXISTS {database_name};"
    query_execution_id = execute_query(database="default", query=query, output_location=output_location)

    if query_execution_id:
        state = wait_for_query_to_complete(query_execution_id)
        if state == "SUCCEEDED":
            print(f"Athena database '{database_name}' created successfully.")
        else:
            print(f"Failed to create Athena database '{database_name}'. Query state: {state}")
    else:
        print(f"Failed to start database creation query for '{database_name}'.")

def create_metadata_table(database_name, table_name, s3_location, output_location):
    """Create an Athena table for S3 metadata."""
    query = f"""
    CREATE EXTERNAL TABLE IF NOT EXISTS {database_name}.{table_name} (
        FileName STRING,
        BucketName STRING,
        ContentType STRING,
        FileSize INT,
        LastModified STRING
    )
    ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
    LOCATION '{s3_location}'
    TBLPROPERTIES ('has_encrypted_data'='false');
    """

    query_execution_id = execute_query(database_name, query, output_location)

    if query_execution_id:
        state = wait_for_query_to_complete(query_execution_id)
        if state == "SUCCEEDED":
            print(f"Athena table '{table_name}' created successfully in database '{database_name}'.")
        else:
            print(f"Failed to create table '{table_name}'. Query state: {state}")
    else:
        print(f"Failed to start table creation query for '{table_name}'.")
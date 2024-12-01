import json
import boto3

# Initialize AWS clients
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')
ses = boto3.client('ses')

# Environment variables (update in AWS Lambda Console or while deploying)
TABLE_NAME = "FileMetadataTable"
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:359533991697:FileUploadNotifications"  # SNS Topic ARN
SENDER_EMAIL = "tsegazeabmulugeta@gmail.com"  # verified SES email
RECIPIENT_EMAIL = "tsegazeabmberhie@gmail.com"  # verified SES email

def lambda_handler(event, context):
    try:
        # Parse the S3 event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_name = event['Records'][0]['s3']['object']['key']

        # Fetch file metadata
        response = s3_client.head_object(Bucket=bucket_name, Key=file_name)
        metadata = {
            "FileName": file_name,
            "BucketName": bucket_name,
            "ContentType": response.get('ContentType'),
            "FileSize": response.get('ContentLength'),
            "LastModified": str(response.get('LastModified'))
        }

        # Store metadata in DynamoDB
        table = dynamodb.Table(TABLE_NAME)
        table.put_item(Item=metadata)

        # Publish SNS notification
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=f"File '{file_name}' uploaded to bucket '{bucket_name}'."
        )

        # Send email via SES
        subject = f"File Uploaded: {file_name}"
        body = f"Metadata: {json.dumps(metadata, indent=4)}"
        ses.send_email(
            Source=SENDER_EMAIL,
            Destination={"ToAddresses": [RECIPIENT_EMAIL]},
            Message={
                "Subject": {"Data": subject},
                "Body": {"Text": {"Data": body}}
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps("Processing completed successfully.")
        }

    except Exception as e:
        print(f"Error processing S3 event: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps("Error processing event.")
        }

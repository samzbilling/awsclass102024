import boto3

sns = boto3.client('sns')

def create_sns_topic(topic_name):
    """Create an SNS topic."""
    try:
        response = sns.create_topic(Name=topic_name)
        topic_arn = response["TopicArn"]
        print(f"SNS topic '{topic_name}' created successfully.")
        return topic_arn
    except Exception as e:
        print(f"Error creating SNS topic: {e}")
        return None

def send_sns_notification(topic_arn, message):
    """Send an SNS notification."""
    try:
        sns.publish(TopicArn=topic_arn, Message=message)
        print(f"SNS notification sent: {message}")
    except Exception as e:
        print(f"Error sending SNS notification: {e}")

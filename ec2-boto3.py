# pip install boto3
# aws configure

import boto3
import os

# EC2 Instance Management using Boto3
# variables
ec2 = boto3.client('ec2')
instance_name = "ec2-with-boto3"
AMI_ID = "ami-06c9bf7b301fc43f1"
key_pair_name = "aws-class-web-server-key"
instance_type = "t2.micro"

# Launch an EC2 instance.
def create_instance(instance_name):
    """Launch an EC2 instance and assign a name."""
    try:
        # Create the instance
        instances = ec2.run_instances(
            ImageId=AMI_ID,
            InstanceType=instance_type,
            KeyName=key_pair_name,
            MinCount=1,  # Number of instances to launch (minimum)
            MaxCount=1,  # Number of instances to launch (maximum)
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': instance_name
                        }
                    ]
                }
            ]
        )
    # Retrieve instance details
        instance_id = instances['Instances'][0]['InstanceId']
        print(f"Instance {instance_name} with ID {instance_id} created successfully!")

        return instance_id
    except Exception as e:
        print(f"Error launching instance: {e}")
        return None


# Retrieve the public IP address of the instance.
# Stop the instance.
# Stop an EC2 instance
def stop_instance(instance_id):
    """Stop an EC2 instance."""
    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} stopped successfully!")
    except Exception as e:
        print(f"Error stopping instance: {e}")
# Start the instance again.
# Terminate the instance.

# Workflow execution
if __name__ == "__main__":   
    #create_instance(instance_name)
    instance_id = create_instance(instance_name)
    stop_instance(instance_id)
# Challenges :
# Use tags to name the instance.
# Create a security group and associate it with the instance.
# Handle errors when attempting to start/stop an already running/stopped instance.
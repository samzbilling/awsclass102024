import boto3
import os
import random
import time


#Exercise 2: DynamoDB CRUD(create/read/update/delete)
#----------------------------------------------------
db = boto3.resource('dynamodb')
table = db.Table("employees")
table.put_item(
    Item={
        "emp_id":"N1234",
        "emp_name":"Jerome",
        "Age":"35"
    }
)
response = table.get_item(
    Key={
        "emp_id":"N1234"
    }
)
print(response["Item"])

table.delete_item(
    Key={
        "emp_id":"N1234"
    }
)

#Exercise 3: EC2 Instance management
#--------------------------------------
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

#create
instance = ec2.create_instances(
    ImageId="ami-0866a3c8686eaeeba",
    InstanceType="t2.micro",
    MaxCount=1,
    MinCount=1
)
print(instance)
#show info(IP)
instanceInfo = client.describe_instances()['Reservations']
for each_instance in instanceInfo:
    for instance in each_instance['Instances']:
        print(instance.get("PublicIpAddress"))
print(instanceInfo)
#Stop
instanceStop = client.stop_instances(
    InstanceIds=[
        "i-024ce21a08fc5d1a4",
        "i-0aacfac66d1f785a2"
    ]
)
print(instanceStop)
#start
instanceStart = client.start_instances(
    InstanceIds=[
        "i-024ce21a08fc5d1a4",
        "i-0aacfac66d1f785a2"
    ]
)
print(instanceStart)
#terminate
instanceTerm = client.terminate_instances(
    InstanceIds=[
        "i-024ce21a08fc5d1a4",
        "i-0aacfac66d1f785a2"
    ]
) 

#Exercise 4: Lamda Function
#---------------------------

#Exercise 5: CloudWatch Logs
#----------------------------
client2 = boto3.client('logs')
messages = ["Request Processed Successfully", "Request Failed",
            "Unknown Response", "Email Sent"]

retention_period_days = 1

log_group = 'AssgLogs'
resp = client2.create_log_group(
    logGroupName=log_group,
    tags={
        'Type': 'Back-end',
        'Frequency': '30 seconds',
        'RetentionPeriod':str(retention_period_days)
    }
)
respStream = client2.create_log_stream(
    logGroupName = 'AssgLogs',
    logStreamName = 'PracticeLogs'
)
for i in range(3):
    log_event= {
        'logGroupName': 'AssgLogs',
        'logStreamName': 'PracticeLogs',
        'logEvents': [
            {
                'timestamp': int(round(time.time() * 1000)),
                'message': messages[random.randint(0, 3)]
            },
        ],
    }
    respStream = client2.put_log_events(**log_event)

client2.delete_log_group(
    logGroupName=log_group
)







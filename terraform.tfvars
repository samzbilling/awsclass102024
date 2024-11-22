# terraform.tfvars

# VPC Variables
vpc_cidr_block              = "10.0.0.0/16"
public_subnet_cidr_blocks  = ["10.0.1.0/24", "10.0.2.0/24"]
private_subnet_cidr_blocks = ["10.0.10.0/24", "10.0.20.0/24"]
vpc_name                    = "main-vpc"

# EC2 Variables
ami           = "ami-063d43db0594b521b"  
instance_type = "t2.micro"
key_name      = "ec2-demo"  # key pair name
ec2_name      = "my-ec2-instance"

# Domain Name
domain_name = "kinglogisticssolutions.com"  
# bucket_name = "midterm-remote-state-bucket"
name        = "environment"
environment = "c4j"

vpc_cidr                    = "10.0.0.0/16"
vpc_name                    = "midterm-us-east-vpc-1"
public_subnet               = [0, 1]
private_subnet              = [2, 3]
cidr_public_subnet          = ["10.0.1.0/24", "10.0.2.0/24"]
cidr_private_subnet         = ["10.0.3.0/24", "10.0.4.0/24"]
us_availability_zone        = ["us-east-1a", "us-east-1b"]

public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGXijg5wWuAZqw3isCBwvWyCqsBb6k6gPBanrD3fKBPS Administrator@DESKTOP-MEPS753"

ec2_ami_id = "ami-012967cc5a8c9f891"

ec2_user_data_install_nginx = ""

domain_name = "berniministries.com"


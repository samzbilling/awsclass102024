# Create AWS VPC in eu-central-1
# CIDR - 10.0.0.0/16
resource "aws_vpc" "vpc-berni-us-east-1" {
  cidr_block = var.vpc_cidr
  
  tags = {    Name = "VPC: berni-us-east-1"  }
}




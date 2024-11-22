terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"  
    }
  }
}

provider "aws" {
  region = "us-west-1"  
}

module "vpc" {
  source = "./modules/vpc"

  vpc_cidr_block = var.vpc_cidr_block
  public_subnet_cidr_blocks = var.public_subnet_cidr_blocks
  private_subnet_cidr_blocks = var.private_subnet_cidr_blocks

  tags = {
    Name = var.vpc_name
  }
}

module "security_groups" {
  source = "./modules/security_groups"
  vpc_id = module.vpc.vpc_id
}

module "ec2" {
  source = "./modules/ec2"

  ami           = var.ami
  instance_type = var.instance_type
  subnet_id     = module.vpc.public_subnet_ids[0]
  key_name      = var.key_name
  vpc_id        = module.vpc.vpc_id
  domain_name   = var.domain_name # Passing domain name to the EC2 module
  security_group_http_id = module.security_groups.security_group_http_id
  security_group_ssh_id = module.security_groups.security_group_ssh_id

  tags = {
    Name = var.ec2_name
  }
}

module "route53" {
  source = "./modules/route53"

  domain_name = var.domain_name
  public_ip   = module.ec2.public_ip
  instance_eip = module.ec2.instance_eip

  tags = {
    Environment = "dev"
  }
}

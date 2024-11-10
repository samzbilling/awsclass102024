# In terraform/main.tf, set up the provider and call your modules.
# This main.tf file calls each module (VPC, security group, and EC2 instance).

# terraform {
#   required_providers {
#     aws = {
#       source = "hashicorp/aws"
#       version = "~> 4.0"
#     }
#   }
# }

provider "aws" {
  region = "us-east-1"
}

# VPC Module block:

module "vpc" {
  source = "./modules/vpc"
}

# Security Groups Module block:

module "security_groups" {
  source = "./modules/security_groups"
  vpc_id = module.vpc.vpc_id            # Pass VPC ID from the vpc module
  ssh_ip = var.ssh_ip                   # Pass the SSH IP from root variables
}
# output "security_group_id" {
#   value = module.security_groups.nginx_sg_id
# }


# EC2 Module block:

module "ec2" {
  source           = "./modules/ec2"
  vpc_id           = module.vpc.vpc_id
  public_subnet_id = module.vpc.public_subnet_id  # Passing public_subnet_id from the vpc module
  security_group   = [module.security_groups.security_group_id]
  # security_group   = [module.security_groups.nginx_sg_id]
  key_name         = var.key_name
}
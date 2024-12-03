# VPC Variables
variable "vpc_cidr_block" {
  type = string
  default = "10.0.0.0/16"
}

variable "public_subnet_cidr_blocks" {
  type    = list(string)
  default = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnet_cidr_blocks" {
  type    = list(string)
  default = ["10.0.10.0/24", "10.0.20.0/24"]
}

variable "vpc_name" {
  type = string
  default = "main-vpc"
}

variable "vpc_id" {
  type = string
  default = "main-vpc"
}

# EC2 Variables
variable "ami" {
  type = string
  default = "ami-0c94855ba95c574c8" # Replace AMI ID
}

variable "instance_type" {
  type = string
  default = "t2.micro"
}

variable "key_name" {
  type = string
  description = "Name of the EC2 key pair"
}

variable "ec2_name" {
  type = string
  default = "my-ec2-instance"
}

# Domain Name
variable "kinglogisticssolutionslls.com" {
  type = string
  description = "The domain name to be used for the website"
}
# modules/ec2/variables.tf

variable "ami" {
  type = string
  description = "The ID of the AMI to use for the instance"
}

variable "instance_type" {
  type = string
  description = "The type of instance to launch"
}

variable "subnet_id" {
  type = string
  description = "The ID of the subnet to launch the instance in"
}

variable "key_name" {
  type = string
  description = "The name of the key pair to use for the instance"
}

variable "tags" {
  type = map(string)
  description = "A map of tags to add to the instance"
  default = {}
}

variable "vpc_id" {
  type = string
  description = "The ID of the VPC"
}

variable "domain_name" {
  type = string
  description = "The domain name to be used for the website" 
}

variable "security_group_ssh_id"{
  type = string
  description = "ID of the SSH security group" 
}

variable "security_group_http_id"{
  type = string
  description = "ID of the HTTP security group" 
}
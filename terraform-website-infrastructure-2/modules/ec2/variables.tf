
# modules/ec2/variables.tf

variable "key_name" {
  description = "The SSH key pair name for EC2 access"
  type        = string
}

variable "security_groups" {
  description = "Security group ID(s) for the EC2 instance"
  type        = list(string)
  #default     = "nginx_sg"
}

variable "public_subnet_id" {
  description = "The public subnet ID for the EC2 instance"
  type        = string
}

variable "vpc_id" {
  description = "The VPC ID where the EC2 instance will be deployed"
  type        = string
}

# variable "ami" {
#   description = "AMI ID for the EC2 instance"
#   type        = string
# }

variable "instance_type" {
  description = "Instance type for the EC2 instance"
  type        = string
  default     = "t2.micro"  # Optional: provide a default value
}







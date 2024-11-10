# Create an EC2 instance with Nginx setup and 
# Set up the EC2 instance, referencing the security group and key_name passed from the root.
# Required provider

resource "aws_instance" "nginx_server" {
  ami                    = "ami-01e3c4a339a264cc9" 
  instance_type          = "t2.micro"
  #subnet_id              = module.vpc.public_subnet_id
  subnet_id              = var.public_subnet_id
  associate_public_ip_address = true
  key_name               = var.key_name
  user_data = file("${path.module}/../../scripts/userdata.sh")


  tags = {
    Name = "nginx_server"
  }
  security_groups = var.security_group
  # security_groups = [module.security_groups.security_group_id] 
  
}

output "nginx_public_ip" {
  value = aws_instance.nginx_server.public_ip
}


variable "key_name" {
  description = "The SSH key pair name for EC2 access"
  type        = string
}

variable "security_group" {
  description = "Security group ID(s) for the EC2 instance"
  type        = list(string)
}

variable "public_subnet_id" {
  description = "The public subnet ID for the EC2 instance"
  type        = string
}

variable "vpc_id" {
  description = "vpc-02e5e06c11a364f8c"
  type        = string
}



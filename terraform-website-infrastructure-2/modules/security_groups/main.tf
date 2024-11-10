
# Define security groups to control access: Configure the security group, using ssh_ip to restrict SSH access.

resource "aws_security_group" "nginx_sg" {
  vpc_id = var.vpc_id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Allow HTTP from all
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.ssh_ip]  # Allow SSH from specified IP
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "nginx_security_group"
  }
}

variable "vpc_id" {
  description = "The VPC ID where the security group will be created"
  type        = string
}

variable "ssh_ip" {
  description = "The CIDR block or IP address allowed to access via SSH"
  type        = string
}

# Output the Security Group ID

output "security_group_id" {
    description = "The ID of the security group"
    value = aws_security_group.nginx_sg.id
}




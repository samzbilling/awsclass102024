# Define Variables in variables.tf:

# Create a variables.tf file to define input variables.
# Create a variables.tf file to define variables for the SSH key and IP address.

variable "key_name" {
  description = "The SSH key pair name for EC2 access"
  type        = string
  default     = "my-ssh-key"
}

variable "ssh_ip" {
  description = "The CIDR block or IP address allowed to access via SSH"
  type        = string
  default     = "74.96.189.98/32"  # Replace YOUR_IP_ADDRESS with your IP
}

variable "vpc_id" {
  description = "The VPC ID where the instance will be deployed"
  type        = string
  default     = "vpc-02e5e06c11a364f8c"
}

variable "public_subnet_id" {
  description = "The public subnet ID for the EC2 instance"
  type        = string
}

# modules/security_groups/variables.tf

variable "vpc_id" {
  description = "The VPC ID where the security group will be created."
  type        = string
  default = "vpc-0b92fdf94ce9e441a"
}

variable "ssh_ip" {
  description = "The SSH IP address allowed in the security group."
  type        = string
}

# In modules/security_groups/variables.tf

variable "vpc_id" {
  description = "The VPC ID where the security group will be created."
  type        = string
}

variable "ssh_ip" {
  description = "The SSH IP address allowed in the security group."
  type        = string
}

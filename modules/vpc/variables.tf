variable "vpc_cidr_block" {
  type = string
  description = "The CIDR block for the VPC"
}

variable "public_subnet_cidr_blocks" {
  type    = list(string)
  description = "List of CIDR blocks for the public subnets"
}

variable "private_subnet_cidr_blocks" {
  type    = list(string)
  description = "List of CIDR blocks for the private subnets"
}

variable "tags" {
  type = map(string)
  description = "A map of tags to add to all"
}
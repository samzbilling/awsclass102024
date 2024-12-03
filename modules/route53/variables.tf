variable "domain_name" {
  type = string
  description = "The domain name to be used for the website"
}

variable "public_ip" {
  type = string
  description = "The public IP address to associate with the domain"
}

variable "tags" {
  type = map(string)
  description = "A map of tags to add to the Route 53 resources"
  default = {}
}

variable "instance_eip" {
  type = string
  description = "The public IP address to associate with the domain"
}
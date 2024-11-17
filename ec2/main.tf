variable "ami_id" {}
variable "instance_type" {}
variable "tag_name" {}
variable "public_key" {}
variable "subnet_id" {}
variable "sg_enable_ssh_https" {}
variable "enable_public_ip_address" {}
variable "user_data_install_nginx" {}

# output "ssh_connection_string_for_ec2" {
#   value = format("%s%s", "ssh -i /home/aws/keys/aws_ec2_terraform aws@", aws_instance.eldtesh_ec2.public_ip)
# }

output "eldtesh_ec2_instance_id" {
  value = aws_instance.eldtesh_ec2.id
}

output "eldtesh_public_ip" {
  value = aws_instance.eldtesh_ec2.public_ip
}

resource "aws_instance" "eldtesh_ec2" {
  ami           = var.ami_id
  instance_type = var.instance_type
  tags = {
    Name = var.tag_name
  }
  key_name                    = "tf_aws_key"
  subnet_id                   = var.subnet_id
  associate_public_ip_address = var.enable_public_ip_address

  user_data = var.user_data_install_nginx

  metadata_options {
    http_endpoint = "enabled"  # Enable the IMDSv2 endpoint
    http_tokens   = "required" # Require the use of IMDSv2 tokens
  }
}

resource "aws_key_pair" "eldtesh_public_key" {
  key_name   = "tf_aws_key"
  public_key = var.public_key
}
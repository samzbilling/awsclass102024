# Create an EC2 instance with Nginx setup and 
# Set up the EC2 instance, referencing the security group and key_name passed from the root.
# Required provider

resource "aws_instance" "nginx_server" {
  #ami           = var.ami
  ami           = "ami-01e3c4a339a264cc9"
  instance_type = var.instance_type
  subnet_id     = var.public_subnet_id
  security_groups = var.security_groups
  associate_public_ip_address = true
  key_name      = var.key_name
  #user_data = var.user_data                         # Accept user_data input
  user_data     =  file("scripts/userdata.sh")

  tags = {
    Name = "nginx_server"
  }

}





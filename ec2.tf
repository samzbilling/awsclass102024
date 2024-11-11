data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["*ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
        name   = "virtualization-type"
        values = ["hvm"]
  }
  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "ec2_instance" {
  ami           = data.aws_ami.ubuntu.id 
  subnet_id = aws_subnet.public_subnet_1.id
  instance_type = "t2.micro"
  key_name = "portfolio-key"
  vpc_security_group_ids = [aws_security_group.allow_tls.id]
  # user_data = ""

  tags = {
    Name = "portfolio-webapp"
  }
}

#resource "aws_key_pair" "deployer" {
#    key_name = "portfolio-key"
#    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD0W6VWMkn9dHeIvn7oqsYu1xOD2WVCH8QlvOAW+k55kQ+tsICi2NX7Io3pRQiwL6s1DDNZrUzTV4aV98blfY14c8WoOLKHeP0Qjl5gbCyijNPnHLlTBDvxKLGhT0wfK8xT4uG37WhWoj7x+FdLw7XcgWCAliGD5IEYoNAjCPTM598kd4qWuwrkqapo4PpkbQCPol+L4GEpjpfntl9g95pYv+wUiYhpWFkUbyl4lqVAgW4Ak10QhY0HVreVrZZswcpnSbkaEI8Yvp5uzBUhSw9gKwEjaKe5vo9SnL03rKPTFo0W1sEznFUWXHFovpVjPOg2IK6rZgpsm6DdZ yilakeseifu@Yilakes-MBP"
#}
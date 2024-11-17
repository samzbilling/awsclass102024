data "aws_subnet" "public_subnet" {
  filter {
    name = "tag:Name"
    values = ["Subnet-Public : Public Subnet 1"]
  }

  depends_on = [    aws_route_table_association.public_subnet_asso  ]
}

resource "aws_instance" "berni_ec2" {
  ami = "ami-012967cc5a8c9f891"
  instance_type = "t2.micro"
  
  tags = {    Name = "EC2 Public subnet 1"  }
  key_name= "tf_keypair"
  subnet_id = data.aws_subnet.public_subnet.id
  vpc_security_group_ids = [aws_security_group.sg_vpc_berni_us_east_1.id]
}

resource "aws_key_pair" "deployer" {
  key_name   = "aws_key"
  public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGVs8ctKnNuGpjSj6r+eLqXw2RMeTpDVLd8cqHrApN99 Administrator@DESKTOP-MEPS753"
}


# output "fetched_info_from_aws" {
#   value = format("%s%s","ssh -i ~/.ssh/aws_ec2_terraform awsami@",aws_instance.berni_ec2.public_dns)
# }
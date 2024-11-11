resource "aws_vpc" "vpc" {
  cidr_block = "10.0.100.0/22"
  enable_dns_hostnames = true

  tags = {
    Name = "webapp-vpc"
  }
}

#create internet gateway and attach to vpc 
resource "aws_internet_gateway" "internet_gateway" {
    vpc_id = aws_vpc.vpc.id

    tags = {
        Name = "int-gw"
    }
}


resource "aws_subnet" "public_subnet_1" {
  vpc_id = aws_vpc.vpc.id
  cidr_block = "10.0.100.0/28"
  availability_zone = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "public-subnet-az1"
  }
}

resource "aws_route_table" "public_route_table" {
    vpc_id = aws_vpc.vpc.id

    route {
        cidr_block = "0.0.0.0/0"
        gateway_id = aws_internet_gateway.internet_gateway.id
    }

    tags = {
        Name = "public-route-table-webapp"
    }
}
resource "aws_route_table_association" "public_table_association" {
    subnet_id = aws_subnet.public_subnet_1.id
    route_table_id = aws_route_table.public_route_table.id
}

# modules/vpc/main.tf

resource "aws_vpc" "main" {
  cidr_block = var.vpc_cidr_block

  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = var.tags
}

resource "aws_subnet" "public" {
  count = length(var.public_subnet_cidr_blocks)

  vpc_id     = aws_vpc.main.id
  cidr_block = element(var.public_subnet_cidr_blocks, count.index)

  
  availability_zone = element(["us-west-1a", "us-west-1b", "us-west-1c"], count.index)

  tags = merge(
    var.tags,
    {
      Name = "public-subnet-${count.index + 1}"
    })
}

resource "aws_subnet" "private" {
  count = length(var.private_subnet_cidr_blocks)

  vpc_id     = aws_vpc.main.id
  cidr_block = element(var.private_subnet_cidr_blocks, count.index)

  
  availability_zone = element(["us-west-1a", "us-west-1b", "us-west-1c"], count.index)

  tags = merge(
    var.tags,
    {
      Name = "private-subnet-${count.index + 1}"
  })
}

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id

  tags = merge(
    var.tags,
    {
      Name = "main-igw"
    })
}

resource "aws_eip" "nat_eip" {
  vpc = true

  tags = merge(
    var.tags,
    {
      Name = "nat-eip"
    })
}

resource "aws_nat_gateway" "nat" {
  allocation_id = aws_eip.nat_eip.id
  subnet_id     = element(aws_subnet.public.*.id, 0)

  tags = merge(
    var.tags,
    {
      Name = "main-nat"
    })

  depends_on = [aws_internet_gateway.gw]
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }

  tags = merge(
    var.tags,
    {
      Name = "public-route-table"
    })
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat.id
  }

  tags = merge(
    var.tags,
    {
      Name = "private-route-table"
    })
}

resource "aws_route_table_association" "public" {
  count = length(aws_subnet.public.*.id)

  subnet_id      = element(aws_subnet.public.*.id, count.index)
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "private" {
  count = length(aws_subnet.private.*.id)

  subnet_id      = element(aws_subnet.private.*.id, count.index)
  route_table_id = aws_route_table.private.id
}
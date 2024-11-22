# VPC Module

This module creates a VPC with public and private subnets across multiple Availability Zones.

## Resources

*   **`aws_vpc`:** Creates a VPC with the specified CIDR block.
*   **`aws_subnet`:** Creates public and private subnets in each Availability Zone.
*   **`aws_internet_gateway`:** Creates an internet gateway for internet access.
*   **`aws_nat_gateway`:** Creates a NAT gateway for private subnet instances to access the internet.
*   **`aws_eip`:** Allocates an Elastic IP for the NAT gateway.
*   **`aws_route_table`:** Creates route tables for public and private subnets.
*   **`aws_route_table_association`:** Associates subnets with their respective route tables.

## Variables

*   **`vpc_cidr_block`:** The CIDR block for the VPC.
*   **`public_subnet_cidr_blocks`:** A list of CIDR blocks for the public subnets.
*   **`private_subnet_cidr_blocks`:** A list of CIDR blocks for the private subnets.
*   **`tags`:** A map of tags to assign to the VPC resources.

## Outputs

*   **`vpc_id`:** The ID of the VPC.
*   **`public_subnet_ids`:** A list of IDs of the public subnets.
*   **`private_subnet_ids`:** A list of IDs of the private subnets.
*   **`nat_eip_id`:** The ID of nat gateway.
# Security Groups Module

This module defines security groups for the EC2 instance.

## Resources

*   **`aws_security_group`:** Creates two security groups:
    *   **SSH access:** Allows inbound SSH traffic from trusted IP addresses.
    *   **HTTP access:** Allows inbound HTTP traffic from any source.

## Variables

*   **`vpc_id`:** The ID of the VPC to create the security groups in.

## Outputs

*   **`security_group_ssh_id`:** The ID of the SSH security group.
*   **`security_group_http_id`:** The ID of the HTTP security group.
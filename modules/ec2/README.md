# EC2 Module

This module deploys an EC2 instance configured as a web server running Nginx.

## Resources

*   **`aws_instance`:** Creates an EC2 instance with the following configurations:
    *   AMI: Specified by the `ami` variable.
    *   Instance type: Specified by the `instance_type` variable.
    *   Subnet: Deployed in the public subnet provided by the `subnet_id` variable.
    *   Key pair: Uses the key pair specified by the `key_name` variable.
    *   Security groups: Attaches the security groups provided by the `security_groups` variable.
    *   IAM instance profile: Associates an IAM role (if provided) for accessing other AWS services.
    *   User data: Executes a script to install Nginx, configure the web server, and set up the website files.

## User Data Script

The user data script performs the following actions:

1.  Installs Nginx.
2.  Creates the necessary directories for the website files.
3.  Sets appropriate ownership and permissions on the website directory.
4.  Configures Nginx to serve the website content.
5.  Restarts Nginx to apply the configuration.

## Variables

*   **`ami`:** The ID of the Amazon Machine Image (AMI) to use for the instance.
*   **`instance_type`:** The type of EC2 instance to launch.
*   **`subnet_id`:** The ID of the subnet to launch the instance in.
*   **`key_name`:** The name of the key pair to use for SSH access to the instance.
*   **`security_groups`:** A list of security group IDs to associate with the instance.
*   **`iam_instance_profile`:** (Optional) The name of the IAM instance profile to attach to the instance.
*   **`tags`:** A map of tags to assign to the instance.

## Outputs

*   **`public_ip`:** The public IP address of the EC2 instance.
*   **`instance_eip`:** The Elastic IP address associated with the instance.
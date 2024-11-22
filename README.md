# Main Module

This is the main Terraform configuration file that orchestrates the deployment of the entire infrastructure.

## Modules

*   **`vpc`:** Creates the VPC and subnet infrastructure.
*   **`security_groups`:** Defines the security groups for the EC2 instance.
*   **`ec2`:** Deploys the EC2 instance with Nginx installed and configured.
*   **`route53`:** Configures the Route 53 records for the domain.

## Variables

*   Defines various variables required by the modules, such as VPC CIDR blocks, AMI ID, instance type, domain name, etc.

## Execution

This file calls the modules in the correct order to ensure dependencies are met and resources are created in the proper sequence.

## Running the Terraform Configuration

**Prerequisites:**

*   **AWS Account:** An active AWS account with necessary permissions.
*   **AWS CLI:** Install and configure the AWS CLI with your credentials.
*   **Terraform:** Install Terraform on your local machine.

**Steps:**

1.  **Configure AWS Credentials:**
    *   Run `aws configure` to set up your AWS access key ID, secret access key, region, and output format.

2.  **Review and Modify Variables:**
    *   Open the `terraform.tfvars` file and update the variables according to your requirements. This includes:
        *   `vpc_cidr_block`, `public_subnet_cidr_blocks`, `private_subnet_cidr_blocks`
        *   `ami`, `instance_type`, `key_name`
        *   `domain_name`, `zone_id`

3.  **Initialize Terraform:**
    *   Navigate to the directory containing your Terraform files.
    *   Run `terraform init` to initialize the working directory and download the necessary providers.

4.  **Plan and Apply:**
    *   Execute `terraform plan` to preview the changes Terraform will make to your infrastructure.
    *   If the plan looks correct, run `terraform apply` to create the resources.

5.  **Verify Deployment:**
    *   Check the AWS Management Console to verify that the resources (VPC, EC2 instance, Route 53 records) have been created successfully.

**Additional Commands:**

*   `terraform destroy`: To delete all the resources created by this configuration.
*   `terraform output`: To view the outputs from the modules (e.g., public IP address).

**Note:**

*   Ensure that your AWS credentials have the necessary permissions to create the resources defined in the configuration.
*   The `terraform.tfvars` file contains the variables used by the modules. You can modify these variables to customize your deployment.
*   Always review the `terraform plan` output carefully before applying the changes to avoid unintended consequences.
# Route53 Module

This module configures Route 53 records for a domain.

## Resources

*   **`aws_route53_record`:** Creates DNS records for the domain:
    *   **A record:** Maps the domain name to the public IP address of the EC2 instance.
    *   **CNAME record:** Creates an alias for the domain name (e.g., `www.example.com`).

## Variables

*   **`domain_name`:** The domain name to configure.
*   **`public_ip`:** The public IP address to associate with the A record.
*   **`instance_eip`:** The Elastic IP address to associate with the A record.
*   **`zone_id`:** The ID of the Route 53 hosted zone.
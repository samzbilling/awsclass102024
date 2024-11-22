output "public_ip" {
  value       = aws_instance.ec2.public_ip
  description = "The public IP address of the EC2 instance"
}

output "instance_eip" {
  value       = aws_eip.eip.public_ip
  description = "The elastic address of the EC2 instance"
}
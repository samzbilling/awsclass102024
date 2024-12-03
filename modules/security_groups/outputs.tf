# Outputs
output "security_group_ssh_id" {
  value = aws_security_group.allow_ssh.id
  description = "ID of the SSH security group"
}

output "security_group_http_id" {
  value = aws_security_group.allow_http.id
  description = "ID of the HTTP security group"
}
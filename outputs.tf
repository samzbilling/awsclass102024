output "eldtesh_vpc_id" {
  value = module.networking.eldtesh_vpc_id
}

output "eldtesh_public_ip" {
  value = module.ec2.eldtesh_public_ip
}

/*output "ec2_ssh_string" {
  value = module.ec2.ssh_connection_string_for_ec2
}

output "hosted_zone_id" {
  value = module.hosted_zone.hosted_zone_id
}*/


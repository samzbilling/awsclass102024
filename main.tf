
module "networking" {
  source                       = "./networking"
  vpc_cidr                     = var.vpc_cidr
  vpc_name                     = var.vpc_name
  cidr_public_subnet           = var.cidr_public_subnet
  us_availability_zone         = var.us_availability_zone
  cidr_private_subnet          = var.cidr_private_subnet
  public_subnet                = var.public_subnet
  private_subnet               = var.private_subnet
}

module "security_group" {
  source                     = "./security-groups"
  ec2_sg_name                = "SG for EC2 to enable SSH(22) and HTTP(80)"
  vpc_id                     = module.networking.eldtesh_vpc_id
  public_subnet_cidr_block   = tolist(module.networking.public_subnet_cidr_block)
}

module "ec2" {
  source                     = "./ec2"
  ami_id                     = var.ec2_ami_id
  instance_type              = "t2.micro"
  tag_name                   = "aws Linux EC2"
  public_key                 = var.public_key
  subnet_id                  = tolist(module.networking.eldtesh_public_subnets)[0]
  sg_enable_ssh_https        = module.security_group.sg_ec2_sg_ssh_http_id
  enable_public_ip_address   = true
  user_data_install_nginx   = templatefile("./template/ec2_install_nginx.sh", {})
}

module "lb_target_group" {
  source                   = "./load-balancer-target-group"
  lb_target_group_name     = "midterm-lb-target-group"
  lb_target_group_port     = 80
  lb_target_group_protocol = "HTTP"
  vpc_id                   = module.networking.eldtesh_vpc_id
  ec2_instance_id          = module.ec2.eldtesh_ec2_instance_id
}

module "alb" {
  source                    = "./load-balancer"
  lb_name                   = "midterm-alb"
  is_external               = false
  lb_type                   = "application"
  sg_enable_ssh_https       = module.security_group.sg_ec2_sg_ssh_http_id
  subnet_ids                = tolist(module.networking.eldtesh_public_subnets)
  tag_name                  = "midterm-alb"
  lb_target_group_arn       = module.lb_target_group.eldtesh_lb_target_group_arn
  ec2_instance_id           = module.ec2.eldtesh_ec2_instance_id
  lb_listner_port           = 80
  lb_listner_protocol       = "HTTP"
  lb_listner_default_action = "forward"
  lb_target_group_attachment_port = 80
}


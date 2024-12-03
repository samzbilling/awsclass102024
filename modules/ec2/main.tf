resource "aws_key_pair" "keypair" {
  key_name   = "my_key_pair"  # Choose a name for your key pair
  public_key = file("~/.ssh/id_rsa.pub") # Path to your public key file
}

# IAM Role for EC2
resource "aws_iam_role" "ec2_role" {
  name = "ec2_role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Effect":
 "Allow",
      "Sid": 
 ""
    }
  ]
}
EOF
}

# IAM Policy for S3 and Secrets Manager Access
resource "aws_iam_policy" "ec2_policy" {
  name = "ec2_policy"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:GetObject"
      ],
      "Resource": "*" 
    },
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue"
      ],
      "Resource": "*" 
    }
  ]
}
EOF
}

# Attach the policy to the role
resource "aws_iam_role_policy_attachment" "ec2_policy_attachment" {
  role       = aws_iam_role.ec2_role.name
  policy_arn = aws_iam_policy.ec2_policy.arn

}

# Instance Profile
resource "aws_iam_instance_profile" "ec2_instance_profile" {
  name = "ec2_instance_profile"
  role = aws_iam_role.ec2_role.name 

}

resource "aws_instance" "ec2" {
  ami                    = var.ami
  iam_instance_profile = aws_iam_instance_profile.ec2_instance_profile.name
  instance_type          = var.instance_type
  associate_public_ip_address = true
  subnet_id              = var.subnet_id
  key_name               = aws_key_pair.keypair.key_name
  security_groups = [var.security_group_ssh_id,var.security_group_http_id] 
  
  lifecycle {
    ignore_changes = [security_groups]

  }

  # User data script directly in the resource block
  user_data = <<EOF
#!/bin/bash
sudo dnf update -y
sudo dnf install -y nginx
sudo systemctl start nginx
sudo systemctl enable nginx

sudo mkdir -p /var/www/mywebsite
sudo chown -R www-data:www-data /var/www/mywebsite
sudo chmod -R 755 /var/www/mywebsite

cat <<EOL > /var/www/mywebsite/index.html 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic 
 HTML Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin:  
 20px;
        }
        nav {
            margin-bottom: 20px;
        }
        nav a {
            margin-right: 15px;
            text-decoration: none;
            color: #007BFF;
        }
        nav a:hover {
            text-decoration: underline;
        }
        section {
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <nav>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
    </nav>

    <section id="about">
        <h2>About Us</h2>
        <p>Welcome to our website! We are dedicated to providing the best service possible.</p>
    </section>

    <section id="contact">
        <h2>Contact Us</h2>
        <p>If you have any questions, feel free to reach out to us at:</p>
        <p>Email: example@example.com</p> 
        <p>Phone: +1 234 567 890</p> 
    </section>

</body>
</html>
EOL


cat <<EOL > /etc/nginx/conf.d/mywebsite.conf
server {
    listen 80;
    server_name ${var.domain_name};  # Accessing domain_name variable from the module
    root /var/www/mywebsite;

    index index.html;

    location / {
        try_files \$uri \$uri/ =404;
    }
}
EOL

sudo systemctl restart nginx
EOF

  tags = var.tags
}

# #Security Group for SSH access
# resource "aws_security_group" "allow_ssh" {
#   name = "allow_ssh"
#   vpc_id = var.vpc_id

#  ingress {
#     from_port   = 22
#     to_port     = 22
#     protocol    = "tcp"
#     cidr_blocks = ["49.36.91.160/32"] #  Restrict this to your IP or a bastion host's IP
#   }

#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   tags = {
#     Name = "allow_ssh"
#   }
# }

# # Security Group for HTTP access
# resource "aws_security_group" "allow_http" {
#   name = "allow_http"
#   vpc_id = var.vpc_id

#   ingress {
#     from_port   = 80
#     to_port     = 80
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   tags = {
#     Name = "allow_http"
#   }
# }

resource "aws_eip" "eip" {
  vpc = true 
}

resource "aws_eip_association" "eip_assoc" {
  instance_id   = aws_instance.ec2.id
  allocation_id = aws_eip.eip.id
}

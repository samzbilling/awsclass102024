# Create a script to install and configure Nginx on startup.

#!/bin/bash

# Update the system and Install Nginx

sudo yum update -y
sudo yum install -y nginx
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx

# Create the directory for storing the website files. This creates the /var/www/mywebsite directory if it doesn't exist.

sudo mkdir -p /var/www/mywebsite

# Copy all website files (including index.html and styles.css) from /tmp/mywebsite to the Nginx web folder (/var/www/mywebsite)

sudo cp -r /tmp/mywebsite/* /var/www/mywebsite  

# Permissions and Ownership: Sets ownership to nginx:nginx and permissions to 755 so that Nginx can read and serve the files.

# Change ownership so Nginx can serve the files

sudo chown -R nginx:nginx /var/www/mywebsite

# Set appropriate permissions for the website directory and files

sudo chmod -R 755 /var/www/mywebsite

# Nginx Configuration: Configures Nginx to serve content from /var/www/mywebsite, listening on port 80.
# Set up Nginx config to serve the website

#sudo cat <<EOL > /etc/nginx/conf.d/mywebsite.conf

sudo bash -c 'cat <<EOL > /etc/nginx/conf.d/mywebsite.conf
server {
    listen 80;
        root /var/www/mywebsite;                 #Path to the directory holding the website files
        index index.html;
  
    location / {
        try_files $uri $uri/ =404;              #Serve the file if it exists, or return 404
    }

}
EOL'

# restart Nginx service

sudo systemctl restart nginx





to deploy your website files to an EC2 instance without using an S3 bucket and without pasting base64-encoded content. In that case, you can still achieve this by using the user_data in Terraform to copy the files directly from your local machine (or a local folder) to the EC2 instance during initialization.

Here's how you can do it:

Approach: Use file() Function in Terraform
Terraform provides the file() function, which allows you to read the contents of a file locally and pass them as variables or directly within the configuration. You can use this to upload your website files into the EC2 instance during initialization.

Steps:
Ensure your local files are ready: Make sure all your website files (index.html, styles.css, logo.png, and the images folder) are ready on your local machine.

Use file() in Terraform to send your files to EC2:

The file() function allows you to include local files (e.g., index.html, styles.css) directly in the user_data script.
You can use the local-exec provisioner in Terraform to copy files from your local system to the EC2 instance.

provider "aws" {
  region = "us-east-1"  # Replace with your AWS region
}

resource "aws_instance" "my_ec2" {
  ami           = "ami-xxxxxxxx"  # Replace with your EC2 AMI ID
  instance_type = "t2.micro"      # Instance type
  key_name      = "your-key-name" # Replace with your SSH key name

  # Security group for HTTP access (port 80)
  security_groups = ["web_sg"]

  # User data to install Nginx and configure the server
  user_data = <<-EOF
    #!/bin/bash
    # Update the system and install Nginx
    sudo yum update -y
    sudo yum install -y nginx
    sudo systemctl start nginx
    sudo systemctl enable nginx
    sudo systemctl status nginx

    # Create directory for website files
    sudo mkdir -p /var/www/mywebsite/images

    # Copy website files from /tmp/mywebsite to the Nginx web directory
    sudo cp -r /tmp/mywebsite/* /var/www/mywebsite/

    # Set ownership and permissions
    sudo chown -R nginx:nginx /var/www/mywebsite
    sudo chmod -R 755 /var/www/mywebsite

    # Configure Nginx to serve website
    sudo bash -c 'cat <<EOL > /etc/nginx/conf.d/mywebsite.conf
    server {
        listen 80;
        root /var/www/mywebsite;
        index index.html;

        location / {
            try_files \$uri \$uri/ =404;
        }

        location /images/ {
            # Serving images from /var/www/mywebsite/images/
        }

        location /logo.png {
            # Serve the logo.png file from /var/www/mywebsite/logo.png
        }
    }
    EOL'

    # Restart Nginx to apply the configuration
    sudo systemctl restart nginx
  EOF

  # Use a local-exec provisioner to upload the website files
  provisioner "local-exec" {
    command = <<-EOT
      scp -i /path/to/your/private/key -r ./mywebsite/* ec2-user@${aws_instance.my_ec2.public_ip}:/tmp/mywebsite/
    EOT
  }

  tags = {
    Name = "MyWebServer"
  }
}


Explanation:
user_data:

This is the script that will be executed on the EC2 instance during its initialization.
The script installs Nginx, creates the necessary directories, and sets up the configuration to serve the website.
local-exec provisioner:

This is used to copy files from your local machine (mywebsite/) to the EC2 instance.
The scp (Secure Copy) command transfers your local files to the EC2 instance.
Replace /path/to/your/private/key with the path to your SSH private key that allows access to the EC2 instance.
Replace ec2-user with the correct username for the EC2 instance (for Amazon Linux, it's usually ec2-user).
The files will be copied to /tmp/mywebsite/ on the EC2 instance.
Accessing the EC2 instance:

After Terraform applies the configuration, the EC2 instance will have the index.html, styles.css, logo.png, and the images folder in the /var/www/mywebsite/ directory, ready to be served by Nginx.
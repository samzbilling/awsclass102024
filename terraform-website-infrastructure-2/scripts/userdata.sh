# Create a script to install and configure Nginx on startup.

#!/bin/bash

# Update the system

sudo yum update -y

# Install Nginx using amazon-linux-extras

sudo amazon-linux-extras enable nginx1
sudo yum install -y nginx

# Check if nginx was installed successfully

if ! command -v nginx &> /dev/null
then
    echo "Nginx installation failed"
    exit 1
fi

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

# Start and enable Nginx service

sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl restart nginx




# Create a script to install and configure Nginx on startup.

#!/bin/bash

# Update and install Nginx

sudo yum update -y
sudo yum install nginx -y

# Create the directory for storing the website files. This creates the /var/www/mywebsite directory if it doesn't exist.

sudo mkdir -p /var/www/mywebsite

# Copy all website files (including index.html and styles.css) from /tmp/mywebsite to the Nginx web folder ((/var/www/mywebsite)

sudo cp -r /tmp/mywebsite/* /var/www/mywebsite  

# Permissions and Ownership: Sets ownership to nginx:nginx and permissions to 755 so that Nginx can read and serve the files.

# Change ownership so Nginx can serve the files

sudo chown -R nginx:nginx /var/www/mywebsite

# Set appropriate permissions for the website directory and files

sudo chmod -R 755 /var/www/mywebsite

# Nginx Configuration: Configures Nginx to serve content from /var/www/mywebsite, listening on port 80.
# Set up Nginx config to serve the website

sudo cat <<EOL > /etc/nginx/conf.d/mywebsite.conf
server {
    listen 80;
    location / {
        root /var/www/mywebsite;
        index index.html index.htm;
    }

}
EOL

# Start and enable Nginx service

sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl restart nginx


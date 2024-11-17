
###  user_data = <<-EOF

#!/bin/bash
# Update packages and install Nginx
apt-get update -y
apt-get install -y nginx

# Create directories for website files
mkdir -p /var/www/mywebsite
sudo chown -R www-data:www-data /var/www/mywebsite

# Create the homepage (index.html)
cat <<EOT > /var/www/mywebsite/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Page</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Welcome to My Website</h1>
        <nav>
            <a href="index.html">Home</a> |
            <a href="about.html">About</a> |
            <a href="contact.html">Contact</a>
        </nav>
    </header>
    <main>
        <h2>Home Page</h2>
        <p>This is the home page of a simple, responsive website.</p>
    </main>
</body>
</html>
EOT

# Create the About page
cat <<EOT > /var/www/mywebsite/about.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>About Us</h1>
        <nav>
            <a href="index.html">Home</a> |
            <a href="about.html">About</a> |
            <a href="contact.html">Contact</a>
        </nav>
    </header>
    <main>
        <h2>About Page</h2>
        <p>Learn more about us on this page.</p>
    </main>
</body>
</html>
EOT

# Create the Contact page
cat <<EOT > /var/www/mywebsite/contact.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Contact Us</h1>
        <nav>
            <a href="index.html">Home</a> |
            <a href="about.html">About</a> |
            <a href="contact.html">Contact</a>
        </nav>
    </header>
    <main>
        <h2>Contact Page</h2>
        <p>Feel free to reach out to us!</p>
    </main>
</body>
</html>
EOT

# Create a basic CSS file for responsiveness
cat <<EOT > /var/www/mywebsite/style.css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
}

header {
    background-color: #333;
    color: #fff;
    padding: 10px 0;
    width: 100%;
}

nav a {
    color: #fff;
    margin: 0 10px;
    text-decoration: none;
}

nav a:hover {
    text-decoration: underline;
}

main {
    padding: 20px;
}

h1, h2 {
    color: #333;
}
@media (max-width: 600px) {
    body {
        font-size: 14px;
    }
}
EOT

# Update Nginx to serve the website files
cat <<EOT > /etc/nginx/sites-available/default
server {
    listen 80;
    root /var/www/mywebsite;
    index index.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }
}
EOT

# Restart Nginx to apply changes
sudo systemctl restart nginx

#EOF

#!/usr/bin/env bash
# Script to install web static files
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow "Nginx HTTP"

# Creating All Required Folders and File
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
sudo touch /data/web_static/releases/test/index.html

PATH_F=/data/web_static/releases/test/index.html

# Adding a Test Content to index file
CONTENT="<html>
<head>
</head>
<body>
    Holberton School
</body>
</html>"

echo "$CONTENT" | sudo tee "$PATH_F"

# Creating A Symbolic Linking
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current

# Granting Ownership
sudo chown -R ubuntu:ubuntu /data/

# Here is the section that configures Nginx Config file
CONF_PATH=/etc/nginx/sites-enabled/default

sudo sed -i "/listen 80 default_server;/a\\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}" "$CONF_PATH"

sudo service nginx restart
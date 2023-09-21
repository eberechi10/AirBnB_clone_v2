#!/usr/bin/env bash

# A script to set a web servers for the AirBnB Clone - Deploy Static project

if ! dpkg -l nginx >/dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

html_data="<html>
  <head>
  </head>
  <body>
    <h1>
     Eberechi
    </h1>
  </body>
</html>"

echo "${html_data}" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

config_to_add="    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
        # Enable directory listing (if desired)
        # autoindex on;
    }"

nginx_config="/etc/nginx/sites-available/default"

if ! grep -q "location /hbnb_static/" "$nginx_config"; then

    sudo awk -v config="$config_to_add" '/^}$/ {print config} {print} ' "$nginx_config" > temp && mv temp "$nginx_config"

    echo "Configuration added."
else
    echo "Configuration already exists."
fi

sudo service nginx restart

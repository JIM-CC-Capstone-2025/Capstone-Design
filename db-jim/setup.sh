#! bin/bash

yum upgrade -y
yum install git curl wget neovim -y
sudo yum install mysql-server -y
sudo systemctl enable mysqld.service --now
sudo mysql_secure_installation


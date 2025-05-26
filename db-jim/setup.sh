#! bin/bash

yum upgrade -y
yum install git curl wget neovim -y
sudo dnf install mysql-server
sudo systemctl enable mysqld.service --now
sudo mysql_secure_installation
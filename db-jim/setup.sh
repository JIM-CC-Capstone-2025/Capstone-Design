#! bin/bash

yum upgrade -y
yum install git curl mysql neovim -y

sudo yum install npm -y
npm init -y
npm install express cors body-parser bcryptjs mysql2 dotenv

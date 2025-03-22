![{DDE64C42-D97D-4130-9C11-0148D38AB54D}](https://github.com/user-attachments/assets/7cafa874-7be0-4e0c-a2da-6c15f8102989)

sudo yum update -y
sudo yum install nginx

sudo systemctl start nginx
sudo systemctl enable nginx

sudo firewall-cmd --permanent --zone=public --add-service=http
sudo firewall-cmd --permanent --zone=public --add-service=https

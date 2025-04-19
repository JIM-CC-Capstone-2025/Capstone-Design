![image](https://github.com/user-attachments/assets/561e34a9-5e4a-4d5f-be46-d9ebbc875e2d)

```
sudo yum install mysql -y


mysql -u root -p

CREATE DATABASE jimtelecomwebpage;
CREATE USER 'jimuser'@'192.168.2.100' IDENTIFIED BY 'EnterPassword';
GRANT ALL PRIVILEGES ON jimtelecomwebpage.* TO 'jimuser'@'192.168.2.100';
FLUSH PRIVILEGES;

USE jimtelecomwebpage;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```



CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    lan_id VARCHAR(255) UNIQUE NOT NULL,
    email_id VARCHAR(255) UNIQUE NOT NULL,
    line_manager VARCHAR(255),
    line_manager_mail_id VARCHAR(255),
    designation VARCHAR(255),
    hashed_password VARCHAR(255) NOT NULL
);
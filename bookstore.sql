CREATE DATABASE IF NOT EXISTS bookstore;
USE bookstore;


CREATE TABLE IF NOT EXISTS  book (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    genre VARCHAR(50),
    price DECIMAL(10, 2),
    quantity INT
);

CREATE TABLE IF NOT EXISTS  transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    transaction_type ENUM('sale', 'restock') NOT NULL,
    quantity INT NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (book_id) REFERENCES book(id)
);

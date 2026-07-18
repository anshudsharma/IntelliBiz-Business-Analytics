CREATE DATABASE intellibiz_db;
USE intellibiz_db;
SHOW DATABASES;

-----------------------

CREATE TABLE companies (
    company_id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(150) NOT NULL,
    industry VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

------------------------

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,

    role ENUM(
        'SUPER_ADMIN',
        'COMPANY_ADMIN',
        'EMPLOYEE'
    ) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (company_id)
        REFERENCES companies(company_id)
        ON DELETE CASCADE
);

--------------------------

CREATE TABLE subscriptions (
    subscription_id INT AUTO_INCREMENT PRIMARY KEY,

    company_id INT NOT NULL,

    plan_type ENUM(
        'FREE',
        'BASIC',
        'PREMIUM'
    ) DEFAULT 'FREE',

    status ENUM(
        'ACTIVE',
        'EXPIRED',
        'CANCELLED'
    ) DEFAULT 'ACTIVE',

    start_date DATE,
    end_date DATE,

    FOREIGN KEY (company_id)
        REFERENCES companies(company_id)
        ON DELETE CASCADE
);

--------------------------

CREATE TABLE audit_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,

    company_id INT,
    user_id INT,

    action VARCHAR(255),

    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (company_id)
        REFERENCES companies(company_id)
        ON DELETE CASCADE,

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE SET NULL
);

--------------------------

CREATE TABLE customers (
    customer_id VARCHAR(50) PRIMARY KEY,

    company_id INT NOT NULL,

    city VARCHAR(100),
    state VARCHAR(50),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (company_id)
        REFERENCES companies(company_id)
        ON DELETE CASCADE
);

--------------------------

CREATE TABLE products (
    product_id VARCHAR(50) PRIMARY KEY,

    company_id INT NOT NULL,

    category VARCHAR(100),

    selling_price DECIMAL(10,2),

    cost_price DECIMAL(10,2),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
        ON DELETE CASCADE
);

--------------------------

CREATE TABLE orders (
    order_id VARCHAR(50) PRIMARY KEY,

    company_id INT NOT NULL,

    customer_id VARCHAR(50),

    order_date DATETIME,

    order_status VARCHAR(50),

    delivery_date DATETIME,

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
        ON DELETE CASCADE,

    FOREIGN KEY(customer_id)
        REFERENCES customers(customer_id)
        ON DELETE SET NULL
);

--------------------------

CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,

    company_id INT NOT NULL,

    order_id VARCHAR(50),

    product_id VARCHAR(50),

    quantity INT DEFAULT 1,

    revenue DECIMAL(12,2),

    shipping_cost DECIMAL(12,2),

    profit DECIMAL(12,2),

    payment_type VARCHAR(50),

    sale_date DATETIME,

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
        ON DELETE CASCADE,

    FOREIGN KEY(order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE,

    FOREIGN KEY(product_id)
        REFERENCES products(product_id)
        ON DELETE SET NULL
);

--------------------------

CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,

    company_id INT,

    product_id VARCHAR(50),

    stock_quantity INT,

    minimum_stock INT,

    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
        ON DELETE CASCADE,

    FOREIGN KEY(product_id)
        REFERENCES products(product_id)
        ON DELETE CASCADE
);

--------------------------

CREATE TABLE reviews (
    review_id VARCHAR(50) PRIMARY KEY,

    company_id INT,

    order_id VARCHAR(50),

    review_score INT,

    review_comment TEXT,

    review_date DATETIME,

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
        ON DELETE CASCADE,

    FOREIGN KEY(order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE
);

--------------------------

CREATE TABLE ml_predictions (
    prediction_id INT AUTO_INCREMENT PRIMARY KEY,

    company_id INT,

    model_name VARCHAR(100),

    prediction_result TEXT,

    accuracy DECIMAL(5,2),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
        ON DELETE CASCADE
);

--------------------------

CREATE TABLE generated_reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY,

    company_id INT,

    report_type VARCHAR(100),

    file_path VARCHAR(255),

    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
        ON DELETE CASCADE
);


--------------------------------

CREATE TABLE alerts (
    alert_id INT AUTO_INCREMENT PRIMARY KEY,

    company_id INT,

    alert_type VARCHAR(100),

    message TEXT,

    status ENUM(
        'UNREAD',
        'READ'
    ) DEFAULT 'UNREAD',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
        ON DELETE CASCADE
);


SELECT COUNT(*) AS total_tables
FROM information_schema.tables
WHERE table_schema = 'intellibiz_db';

SHOW TABLES;

-- Disable foreign key checks temporarily------------

SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE reviews;
TRUNCATE TABLE sales;
TRUNCATE TABLE orders;
TRUNCATE TABLE products;
TRUNCATE TABLE customers;

SET FOREIGN_KEY_CHECKS = 1;


-- --------------------------------------- --


SHOW COLUMNS FROM customers;


ALTER TABLE customers
ADD COLUMN zip_code VARCHAR(20);

SHOW COLUMNS FROM customers;
SELECT * FROM companies;

-- test company --

INSERT INTO companies
(
    company_id,
    company_name,
    industry
)
VALUES
(
    1,
    'IntelliBiz Test Company',
    'E-Commerce'
);
SELECT * FROM companies;
-- ------------------------- correction of all data bases --
SHOW COLUMNS FROM products;
ALTER TABLE products
DROP COLUMN selling_price,
DROP COLUMN cost_price;

ALTER TABLE products
ADD COLUMN weight DECIMAL(10,2),
ADD COLUMN length DECIMAL(10,2),
ADD COLUMN height DECIMAL(10,2),
ADD COLUMN width DECIMAL(10,2);

SHOW COLUMNS FROM products;


SHOW COLUMNS FROM orders;
ALTER TABLE orders
CHANGE COLUMN order_status status VARCHAR(50);

ALTER TABLE orders
CHANGE COLUMN order_date purchase_date DATETIME;

ALTER TABLE orders
CHANGE COLUMN delivery_date delivered_date DATETIME;

ALTER TABLE orders
ADD COLUMN approved_date DATETIME;

ALTER TABLE orders
ADD COLUMN estimated_delivery_date DATETIME;
SHOW COLUMNS FROM orders;


SHOW COLUMNS FROM sales;
ALTER TABLE sales
ADD COLUMN customer_id VARCHAR(50);

ALTER TABLE sales
ADD COLUMN selling_price DECIMAL(12,2);

ALTER TABLE sales
ADD COLUMN estimated_cost DECIMAL(12,2);

ALTER TABLE sales
CHANGE COLUMN payment_type payment_method VARCHAR(50);
SHOW COLUMNS FROM sales;


SHOW COLUMNS FROM reviews;
ALTER TABLE reviews
CHANGE COLUMN review_score rating INT;

ALTER TABLE reviews
CHANGE COLUMN review_comment comment TEXT;
SHOW COLUMNS FROM reviews;
SHOW CREATE TABLE reviews;
DROP TABLE reviews;

CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    review_id VARCHAR(50),
    company_id INT,
    order_id VARCHAR(50),
    rating INT,
    comment TEXT,
    review_date DATETIME,

    FOREIGN KEY (company_id)
        REFERENCES companies(company_id)
        ON DELETE CASCADE,

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE
);


-- verifucation of wharehouse --

SELECT COUNT(*) FROM customers;

SELECT COUNT(*) FROM products;

SELECT COUNT(*) FROM orders;

SELECT COUNT(*) FROM sales;

SELECT COUNT(*) FROM reviews;


SHOW COLUMNS FROM sales;


SHOW COLUMNS FROM products;

DESCRIBE sales;


DESCRIBE products;

DESCRIBE reviews;


DESCRIBE ml_predictions;
--   ml ############################## --
SELECT
    MIN(sale_date),
    MAX(sale_date),
    COUNT(*)
FROM sales;



DESCRIBE companies;


SELECT *
FROM companies;



SELECT *
FROM ml_predictions;


DESCRIBE generated_reports;


ALTER TABLE generated_reports
ADD COLUMN report_content LONGTEXT;
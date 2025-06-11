CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
); 

INSERT INTO students (name, email, age) VALUES
('John Smith', 'john.smith@email.com', 20),
('Emma Johnson', 'emma.j@email.com', 22),
('Michael Brown', 'michael.b@email.com', 19),
('Sophia Davis', 'sophia.d@email.com', 21),
('William Wilson', 'william.w@email.com', 23),
('Olivia Martinez', 'olivia.m@email.com', 20),
('James Taylor', 'james.t@email.com', 22),
('Ava Anderson', 'ava.a@email.com', 19),
('Benjamin Thomas', 'benjamin.t@email.com', 21),
('Isabella Jackson', 'isabella.j@email.com', 20),
('Lucas White', 'lucas.w@email.com', 22),
('Mia Harris', 'mia.h@email.com', 19),
('Ethan Martin', 'ethan.m@email.com', 21),
('Charlotte Thompson', 'charlotte.t@email.com', 20),
('Alexander Garcia', 'alexander.g@email.com', 23);
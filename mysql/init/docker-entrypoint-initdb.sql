CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    roll_number VARCHAR(20) UNIQUE NOT NULL,
    city VARCHAR(100)
);

INSERT INTO students (name, age, roll_number, city) VALUES
    ('John Doe', 18, 'R001', 'New York'),
    ('Jane Smith', 19, 'R002', 'Los Angeles'),
    ('Mike Johnson', 20, 'R003', 'Chicago'),
    ('Sarah Williams', 18, 'R004', 'Houston'),
    ('David Brown', 19, 'R005', 'Phoenix'),
    ('Emily Davis', 20, 'R006', 'Philadelphia'),
    ('James Wilson', 18, 'R007', 'San Antonio'),
    ('Emma Taylor', 19, 'R008', 'San Diego'),
    ('Daniel Anderson', 20, 'R009', 'Dallas'),
    ('Olivia Martinez', 18, 'R010', 'San Jose'),
    ('William Thomas', 19, 'R011', 'Austin'),
    ('Sophia Garcia', 20, 'R012', 'Jacksonville'),
    ('Alexander Lee', 18, 'R013', 'Fort Worth'),
    ('Isabella Lopez', 19, 'R014', 'Columbus'),
    ('Michael King', 20, 'R015', 'Charlotte'),
    ('Ava Wright', 18, 'R016', 'Indianapolis'),
    ('Ethan Scott', 19, 'R017', 'Seattle'),
    ('Mia Green', 20, 'R018', 'Denver'),
    ('Lucas Baker', 18, 'R019', 'Boston'),
    ('Victoria Hall', 19, 'R020', 'Nashville');
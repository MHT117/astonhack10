create DATABASE CUSTOMER_DATA
CREATE TABLE IF NOT  exists Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each user
    Username VARCHAR(255) UNIQUE NOT NULL, -- User's username (must be unique)
    Password VARCHAR(255) NOT NULL        -- User's password (consider hashing)
    salary INT not null 
    tax  int not null
);

-- Example of adding a user (Note: In real applications, securely hash the password before storing it)
INSERT INTO Users (Username, Password) VALUES ('john_doe', 'hashed_password_here'); 
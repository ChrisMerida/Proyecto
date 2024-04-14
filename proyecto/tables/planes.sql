CREATE TABLE IF NOT EXISTS planes (
    tailnum VARCHAR(10) PRIMARY KEY,
    year YEAR,
    type VARCHAR(100),
    manufacturer VARCHAR(100),
    model VARCHAR(50),
    engines INT,
    seats INT,
    speed FLOAT,
    engine VARCHAR(50)
);

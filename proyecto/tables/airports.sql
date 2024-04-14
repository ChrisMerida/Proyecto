CREATE TABLE IF NOT EXISTS airports (
    airport_code VARCHAR(5),
    name VARCHAR(255),
    lat FLOAT,
    lon FLOAT,
    alt INT,
    tz INT,
    dst CHAR(1),
    tzone VARCHAR(40)
);
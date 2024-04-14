CREATE TABLE IF NOT EXISTS weather (
    origin VARCHAR(5),
    year INT,
    month INT,
    day INT,
    hour INT,
    temp FLOAT,
    dewp FLOAT,
    humid FLOAT,
    wind_dir FLOAT,
    wind_speed FLOAT,
    wind_gust FLOAT,
    precip FLOAT,
    pressure FLOAT,
    visib FLOAT,
    time_hour TIMESTAMP
);
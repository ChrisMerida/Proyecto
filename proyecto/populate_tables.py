import pandas as pd
from sqlalchemy import create_engine
from db_config import conn_string

# Create a database engine
engine = create_engine(conn_string)


def load_data(source_file, table_name):
    """Load data from a CSV file into a specified table in the database."""
    df = pd.read_csv(source_file)
    df.to_sql(table_name, con=engine, if_exists='append', index=False)
    print(f"Loaded {len(df)} records into {table_name}.")


def main():
    # Directory where validated data is stored
    valid_data_dir = './valid'

    # Load validated data into tables
    load_data(f"{valid_data_dir}/planes.csv", 'planes')
    load_data(f"{valid_data_dir}/airlines.csv", 'airlines')
    load_data(f"{valid_data_dir}/airports.csv", 'airports')
    load_data(f"{valid_data_dir}/weather.csv", 'weather')
    load_data(f"{valid_data_dir}/flights.csv", 'flights')


if __name__ == "__main__":
    main()

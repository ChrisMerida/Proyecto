import pandas as pd
from sqlalchemy import create_engine, inspect
from db_config import db_config, conn_string
import os

# Create a database engine
engine = create_engine(conn_string)


def sql_to_pandas_type(sql_type):
    """Map SQL data types to pandas-compatible data types."""
    if 'INT' in str(sql_type):
        return 'int64'
    elif 'VARCHAR' in str(sql_type) or 'TEXT' in str(sql_type):
        return 'object'
    elif 'FLOAT' in str(sql_type) or 'DOUBLE' in str(sql_type):
        return 'float64'
    elif 'DATE' in str(sql_type) or 'TIME' in str(sql_type):
        return 'datetime64[ns]'
    else:
        return 'object'  # Default catch-all for other types


def save_valid_data(df, source_file, valid_dir):
    """Save the validated data to a new CSV file in the specified 'valid' directory."""
    if not os.path.exists(valid_dir):
        os.makedirs(valid_dir)
    valid_file_path = os.path.join(valid_dir, os.path.basename(source_file))
    df.to_csv(valid_file_path, index=False)
    print(f"Valid data saved to {valid_file_path}.")


def validate_data_types(source_file, table_name, valid_dir):
    """Validate data types according to the table schema in the database, report validity, and save valid data."""
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name)
    schema = {col['name']: sql_to_pandas_type(col['type']) for col in columns}

    # Parse dates if datetime columns are present and remove timezone if needed
    date_cols = [col for col, dtype in schema.items() if dtype == 'datetime64[ns]']
    df = pd.read_csv(source_file, parse_dates=date_cols)

    mismatches = []
    for column, dtype in schema.items():
        if column in df.columns:
            if dtype == 'datetime64[ns]':
                # Convert timezone-aware datetime to timezone-naive
                if df[column].dt.tz is not None:
                    df[column] = df[column].dt.tz_localize(None)
            try:
                df[column] = df[column].astype(dtype)
            except ValueError:
                print(f"    Difference in {column} data type: {dtype} vs {df[column].dtype}")
                mismatches.append(column)
        else:
            df.drop(column, axis=1, inplace=True)  # Drop columns not in the schema

    if mismatches:
        print(f"Data type mismatches in {table_name} for columns: {', '.join(mismatches)}")
    else:
        print(f"All data types match the schema for {table_name}.")
        save_valid_data(df, source_file, valid_dir)  # Save valid data


def main():
    # Base directory for data source
    data_base_dir = './normalized'
    # Directory where valid data will be saved
    valid_data_dir = './valid'

    # Validate data types for each table and save valid data
    validate_data_types(f"{data_base_dir}/planes.csv", 'planes', valid_data_dir)
    validate_data_types(f"{data_base_dir}/airlines.csv", 'airlines', valid_data_dir)
    validate_data_types(f"{data_base_dir}/airports.csv", 'airports', valid_data_dir)
    validate_data_types(f"{data_base_dir}/weather.csv", 'weather', valid_data_dir)
    validate_data_types(f"{data_base_dir}/flights.csv", 'flights', valid_data_dir)


if __name__ == "__main__":
    main()

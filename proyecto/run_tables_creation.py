import os
import pymysql
from db_connection import get_connection, close_connection


def execute_sql_file(sql_file):
    """Executes a SQL file based on its path."""
    connection = get_connection()
    if connection:
        try:
            with open(sql_file, 'r') as file:
                sql = file.read()
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()
                print(f"Executed '{sql_file}' successfully.")
        except pymysql.MySQLError as e:
            print(f"Error executing '{sql_file}': {e}")
        finally:
            close_connection(connection)


def create_tables():
    """Runs SQL scripts in a specified order to create tables."""
    sql_files_dir = './tables'
    # List of SQL files
    sql_files = [
        'planes.sql',
        'airlines.sql',
        'airports.sql',
        'weather.sql',
        'flights.sql'
    ]
    for filename in sql_files:
        file_path = os.path.join(sql_files_dir, filename)
        if os.path.exists(file_path):
            execute_sql_file(file_path)
        else:
            print(f"File {filename} does not exist in the directory {sql_files_dir}.")


if __name__ == "__main__":
    create_tables()

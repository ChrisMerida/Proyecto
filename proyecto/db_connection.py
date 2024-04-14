import pymysql
from db_config import db_config


def get_connection():
    """Create and return a database connection."""
    try:
        connection = pymysql.connect(
            host=db_config['host'],
            database=db_config['database'],
            user=db_config['user'],
            password=db_config['password'],
            port=db_config['port']
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Error while connecting to MySQL: {e}")
        return None


def close_connection(connection):
    """Close the given database connection."""
    if connection:
        connection.close()
        print("MySQL connection is closed automatically by context manager")

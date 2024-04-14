# Database configuration settings
db_config = {
    'host': 'XXXXXXXX',
    'database': 'proyecto_db',
    'user': 'admin_mysql',
    'password': 'XXXXXXXX',
    'port': 3306
}

conn_string = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

#CREDENCIALES MODIFICADAS POR SEGURIDAD
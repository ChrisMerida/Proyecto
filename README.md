# Proyecto - Flights
## Video
[Video explicación](https://youtu.be/OBFbRGY-41A)


## Instalar librerias
```bash
# Crear entorno virtual (venv)
python -m venv venv

# Activar el entorno virtual
source venv/bin/activate

# Instalar las librerias de Python
# (Asegúrate de estar en la carpeta del proyecto)
pip install -r requirements.txt
```

## Configuración de base de datos
Para el proyecto utilice una base de datos MySQL corriendo en RDS. 
### Parametros
Para conectarse a la instancia de SQL es necesario cambiar los valores en el diccionario de configuración definido en `db_config.py`.
```python
db_config = {
    'host': 'XXXXXXXX',  # Host name de instancia en RDS
    'database': 'proyecto_db',  # Nombre de la base de datos 
    'user': 'admin_mysql',  # Usuario administrador
    'password': 'XXXXXXXX',  # Contraseña para usuario admin_mysql
    'port': 3306  # Puerto de conexión
}
```
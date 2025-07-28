from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv


# ? Vamos a crear la conexión con la BD:


# * 
load_dotenv()


# * Nos traemos los datos necesarios:
usuario = os.getenv('USER_BD')
contrasena = os.getenv('PASS_BD')
host = os.getenv('HOST_BD')
puerto = os.getenv('PORT_BD')
nombre_bd = os.getenv('NAME_BD')


# ? Primero validamos que los datos existan:
assert all([usuario, contrasena, host, puerto, nombre_bd]), "Faltan variables de entorno"


# * Ahora creamos la conexión
engine = create_engine(f"mysql+pymysql://{usuario}:{contrasena}@{host}:{puerto}/{nombre_bd}")




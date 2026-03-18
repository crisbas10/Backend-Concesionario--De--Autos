import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Cargamos las variables del archivo .env
load_dotenv()

# Obtenemos la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("No se encontró DATABASE_URL en el archivo .env")

# Creamos el motor de SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)
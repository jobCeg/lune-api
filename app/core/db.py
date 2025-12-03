import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import OperationalError

# Cargar variables de entorno
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def create_connection():
    """Crea y retorna una conexión a PostgreSQL."""
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        print("Conexión a PostgreSQL exitosa")
        return connection
    except OperationalError as e:
        print(f"Error al conectar a PostgreSQL: {e}")
        return None

# Prueba rápida
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        conn.close()


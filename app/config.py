import os
from datetime import timedelta
import logging

class Config:
    # Configuración básica
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

    SECRET_KEY = os.getenv("SECRET_KEY", "9b3f37d1a27a46f4ac33dfc34a1c24e9")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración de la base de datos con mejor manejo de conexiones
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
        'pool_timeout': 20,
        'max_overflow': 0,
        'pool_size': 5
    }

    # Configuración de la sesión
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)

    # Configuración de archivos estáticos
    STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

    # Configuración de subida de archivos
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

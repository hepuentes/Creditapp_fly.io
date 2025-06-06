# Usar una imagen de Python compatible con Fly.io
FROM python:3.11.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias y instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Ejecutar la aplicación con Gunicorn (recomendado para producción)
CMD ["gunicorn", "-c", "gunicorn_config.py", "run:app"]

# Usa una imagen base de Python 3.12
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el script de Python al contenedor
COPY main.py .

# Establece el comando por defecto para ejecutar el script
CMD ["python", "main.py"]

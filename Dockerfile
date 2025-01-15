# Usa una imagen base de Python 3.12
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Se instalan las Dependencias
COPY requirements.txt /app/ #se agrega el destino
RUN pip install --no-cache-dir -r requirements.txt

# Instalamos pytest
RUN pip install pytest

# Copia el script de Python al contenedor
COPY main.py /app/

# Establece el comando por defecto para ejecutar el script
CMD ["python", "main.py"]

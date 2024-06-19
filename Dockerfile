# Basis-Image
FROM python:3.12-slim-bookworm

# Arbeitsverzeichnis setzen
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Anwendungsdateien kopieren
COPY . .

# Startbefehl
CMD ["python", "./main.py"]

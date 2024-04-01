# Recommendation-api

Para ejecutar usando docker:
```
docker-compose up --build
```

Para ejecutar directamente con python:
Lo primero que tienen que hacer es crear el environment:
```
python3 -m venv ./myenv
```
Luego, tiene que activarlo esto lo hacen siempre que necesiten ejecutar el script, lo primero es solo la primera vez.
```
source ./myenv/bin/activate
```
Finalmente, para instalar las dependecias deben hacer esto:
```
pip install -r requirements.txt
```
Lo unico que tienen que hacer siempre es activar el env.

Luego se ejecuta con:
```
uvicorn app:app --host 127.0.0.1 --port $PORT (o %PORT% para windows) 
```

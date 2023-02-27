## workflow en Linux
```bash
# python3 en linux; py en windows

# Crear el entorno la primera vez
python3 -m venv venv

# Activar el entorno
source venv/bin/activate

# Trabajar (requiere: Activar el entorno)
# pip3 install locust
# pip3 freeze > requirements.txt
# Instala las dependencias en el entorno
pip3 install -r requirements.txt
# Ejecuta la prueba de carga
locust
# locust --users 10 --spawn-rate 1 -H http://your-server.com --locustfile

# Desactivar el entorno (requiere: Activar el entorno)
deactivate
```
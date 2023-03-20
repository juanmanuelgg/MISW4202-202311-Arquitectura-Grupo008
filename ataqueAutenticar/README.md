## workflow en Linux
```bash
# Crear el entorno la primera vez
python3 -m venv venv

# Activar el entorno
source venv/bin/activate

# Trabajar (requiere: Activar el entorno)
# pip3 install requests
# pip3 freeze > requirements.txt
# Instala las dependencias en el entorno
pip3 install -r requirements.txt
# Ejecuta la prueba de carga
python3 main.py

# Desactivar el entorno (requiere: Activar el entorno)
deactivate
```
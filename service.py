import json
import os

# Función para cargar datos desde un archivo JSON
def cargar_datos():
    try:
        with open('pacientes.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def generar_id_autoincremental():
    # Obtenemos el valor actual del ID
    id_actual = 1

    # Verificamos si el archivo de datos existe
    if os.path.exists('datos.json'):
        # Cargamos los datos del archivo
        pacientes = cargar_datos()

        # Obtenemos el último ID de la lista de pacientes
        id_actual = pacientes[-1]['id'] + 1

    return id_actual
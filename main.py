import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite solicitudes desde cualquier origen
# O, para restringir a un origen específico:
# CORS(app, origins=["http://localhost:4200"])

# Función para cargar datos desde un archivo JSON
def cargar_datos():
    try:
        with open('pacientes.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

# Función para guardar datos en un archivo JSON
def guardar_datos(datos):
    with open('pacientes.json', 'w') as archivo:
        json.dump(datos, archivo, indent=2)

# Ruta para obtener todos los pacientes
@app.route('/api/pacientes', methods=['GET'])
def obtener_pacientes():
    pacientes = cargar_datos()
    return jsonify(pacientes)

# Ruta para agregar un nuevo paciente
@app.route('/api/pacientes', methods=['POST'])
def agregar_paciente():
    pacientes = cargar_datos()
    nuevo_paciente = {
        'id': len(pacientes) + 1,
        'nombre': request.json['nombre'],
        'edad': request.json['edad'],
        'diagnostico': request.json['diagnostico']
    }
    pacientes.append(nuevo_paciente)
    guardar_datos(pacientes)
    return jsonify({'mensaje': 'Paciente agregado correctamente'})

# Ruta para actualizar información de un paciente
@app.route('/api/pacientes/<int:id_paciente>', methods=['PUT'])
def actualizar_paciente(id_paciente):
    pacientes = cargar_datos()
    for paciente in pacientes:
        if paciente['id'] == id_paciente:
            paciente['nombre'] = request.json['nombre']
            paciente['edad'] = request.json['edad']
            paciente['diagnostico'] = request.json['diagnostico']
            guardar_datos(pacientes)
            return jsonify({'mensaje': 'Información del paciente actualizada correctamente'})
    return jsonify({'mensaje': 'No se encontró un paciente con ese ID'})

# Ruta para eliminar un paciente
@app.route('/api/pacientes/<int:id_paciente>', methods=['DELETE'])
def eliminar_paciente(id_paciente):
    pacientes = cargar_datos()
    for paciente in pacientes:
        if paciente['id'] == id_paciente:
            pacientes.remove(paciente)
            guardar_datos(pacientes)
            return jsonify({'mensaje': 'Paciente eliminado correctamente'})
    return jsonify({'mensaje': 'No se encontró un paciente con ese ID'})

if __name__ == '__main__':
    app.run(debug=True)

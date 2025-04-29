from flask import Flask, request, jsonify

app= Flask(__name__)

#Lista de nombres para almacenar los usuarios
usuarios = []

#Servicios GET que devuelve la informacion general
@app.route('/info', methods=['GET'])
def obtener_informacion():
    return jsonify({
        "mensajes": "Bienvenidos a mi API de almacenamiento de usuarios",
        "version": "1.0.0",
        "autor": "Ian Padua Cuevas",
    })
# Servicio POST que recibe usuarios y correos y los almacena en la lista
@app.route('/usuarios', methods=['POST'])
def agregar_usuarios():
    data= request.get_json()
    if not data or 'nombre' not in data or 'correo' not in data:
        return jsonify({'error': 'Faltan datos (nombre o correo)'}), 400

    usuario = {
    'nombre': data['nombre'],
    'correo': data['correo']
}
    usuarios.append(usuario)
    return jsonify({"mensaje": "usuario agregado exitosamente", "usuario": usuario}), 201
        
# Servicio GET que devuelve la lista de usuarios almacenados
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify({'usuarios': usuarios}), 200

if __name__ == '__main__':
    app.run(debug= True, port=5000)



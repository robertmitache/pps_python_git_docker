#app.py
from bayeta import frotar, insertar_frases
from mongodb_script import inicializar, instanciar
from flask import Flask, jsonify, request, render_template
from random import choice

# Llamada a la función inicializar para asegurar datos en la base de datos
inicializar('frases.txt')
cliente_mongo, frases_auspiciosas = instanciar()

app = Flask(__name__)

@app.route('/')
def pagina_principal():
	# Obtener una frase auspiciosa aleatoria
	frase_aleatoria = frotar(1)[0]

	# Lista de imagenes disponibles en la carpeta static
	imagenes = [
		'git.png',
		'docker.png',
		'docker-compose.png',
		'mongodb.png'
	]

	# Renderizamos la plantilla con una frase y una imagen aleatoria
	return render_template('index.html', frase=frase_aleatoria, imagen_aleatoria=choice(imagenes))

@app.route('/frotar/<int:n_frases>')
def obtener_frases_auspiciosas(n_frases):
	frases_auspiciosas = frotar(n_frases)
	return jsonify({"frases_auspiciosas": frases_auspiciosas})

@app.route('/frotar/add', methods=['POST'])
def agregar_frases():
    data = request.get_json()
    file_path = data.get('file_path')

    if file_path:
        insertar_frases(file_path, frases_auspiciosas)
        return jsonify({"message": "Frases agregadas correctamente"}), 200
    else:
        return jsonify({"error": "Parámetro 'file_path' no proporcionado"}), 400

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)



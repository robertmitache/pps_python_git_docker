#app.py
from bayeta import frotar
from mongodb_script import inicializar
from flask import Flask, jsonify

# Llamada a la función inicializar para asegurar datos en la base de datos
inicializar('frases.txt')

app = Flask(__name__)

@app.route('/')
def hello_world():
	print(frotar(3)) # Imprimir 3 frases auspiciosas
	return 'Hola, Mundo'

@app.route('/frotar/<int:n_frases>')
def obtener_frases_auspiciosas(n_frases):
	frases_auspiciosas = frotar(n_frases)
	return jsonify({"frases_auspiciosas": frases_auspiciosas})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)



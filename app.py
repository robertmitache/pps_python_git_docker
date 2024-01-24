#app.py
from bayeta import frotar
from flask import Flask, jsonify

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
	app.run(debug=True)



# bayeta.py
import random
from mongodb_script import consultar
from mongodb_script import add
import json

def frotar(n_frases=1):
	return consultar(n_frases)

def insertar_frases(file_path, frases_auspiciosas):
	#Leer datos desde el archivo JSON
	with open(file_path, 'r') as file:
		data = json.load(file)

	# Obtener la lista de frases desde el archivo JSON
	frases = data.get('frases', [])

	# Llamar a la función de inserción de MongoDB
	add(frases, frases_auspiciosas)

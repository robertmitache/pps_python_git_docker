# mongodb_script.py
from pymongo import MongoClient

def instanciar():
	# Conexión con el motor de Mongo
	cliente_mongo = MongoClient('mongodb://mongo:27017/')

	# Conexión con la BD (la crea si no existe)
	bd = cliente_mongo['bayeta']

	# Conexión con la tabla (llamada colección en Mongo)
	frases_auspiciosas = bd['frases_auspiciosas']

	return cliente_mongo, frases_auspiciosas

def add(frases, frases_auspiciosas):
	# Convertimos cada elemento en un dict
	frases_dict = [{"frase": frase} for frase in frases]

	# Inserción de datos
	frases_auspiciosas.insert_many(frases_dict)

def inicializar(file_path):
	# Instanciación
	cliente_mongo, frases_auspiciosas = instanciar()

	try:
		# Comprobamos que no se haya inicializado previamente
		if frases_auspiciosas.count_documents({}) == 0:
			# Leer datos desde el archivo
			with open(file_path, 'r') as file:
				datos = [{"frase": line.strip()} for line in file]

			# Inserción de datos
			add(datos, frases_auspiciosas)
	finally:
		# Cerrar cliente
		cliente_mongo.close()

def consultar(n_frases):
	# Instanciación
	cliente_mongo, frases_auspiciosas = instanciar()

	try:
		# Obtener frases aleatorias
		frases_aleatorias = list(frases_auspiciosas.aggregate([{'$sample': {'size': n_frases}}]))

		# Devolver las frases
		return [frase['frase'] for frase in frases_aleatorias]
	finally:
		# Cerrar cliente
		cliente_mongo.close()

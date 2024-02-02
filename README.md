# La Bayeta de la Fortuna

La Bayeta de la Fortuna es una aplicación web sencilla que proporciona frases auspiciosas de manera aleatoria cada vez que accedes a la página.

## Funcionalidades

- Muestra un saludo simple en la página principal.
- Proporciona frases auspiciosas en la ruta `/frotar/<n_frases>` en formato JSON.

## Ejecución con Docker Compose

1. Asegúrate de tener Docker y Docker Compose instalado en tu máquina.
2. Crea una red de Docker ejecutando el siguiente comando en la raíz del proyecto: `docker network create bayeta-network`.
3. Crea y ejecuta los servicios de Docker utilizando el siguiente comando en la raíz del proyecto: `docker-compose up -d`.
	- Esto construirá las imágenes y ejecutará los contenedores para la aplicación y MongoDB en segundo plano.
4. Accede a `http://localhost:5000` en tu navegador.


## Endpoints

- `/`: Página principal con unas foto aleatoria y una frase auspiciosa aleatoria.
- `/frotar/<n_frases>`: Obtiene `n_frases` frases auspiciosas.
- `/frotar/add` (Método POST): Permite agregar nuevas frases auspiciosas. Envía un JSON con el siguiente formato:

	```json
	{
		"frases": [
			"Nueva frase 1",
			"Nueva frase 2",
			"Nueva frase 3"
		]
	}

## Contribuciones

Para este gran proyecto ha colaborado mi gran amigo Rafael Ibáñez Durán!!

## Notas de la Versión

### Versión 1.7

- Nuevo endpoint `/frotar/add` para agregar frases auspiciosas.
- Diversas mejoras y correcciones en la aplicación.
- Modificación de página principal `/` con una foto aleatoria y una frase auspiciosa aleatoria.

*Proyecto desarrollado como parte de la práctica de Puesta en Producción Segura "La Bayeta de la Fortuna".*

# La Bayeta de la Fortuna

La Bayeta de la Fortuna es una aplicación web sencilla que proporciona frases auspiciosas de manera aleatoria cada vez que accedes a la página.

## Funcionalidades

- Muestra un saludo simple en la página principal.
- Proporciona frases auspiciosas en la ruta `/frotar/<n_frases>` en formato JSON.

### Ejecución Local (sin Docker)

1. Asegúrate de tener Python instalado.
2. Crea y activa un entorno virtual (opcional, pero recomendado).
3. Instala las dependencias con `pip install -r requirements.txt`.
4. Ejecuta la aplicación con `python app.py`.
5. Accede a `http://localhost:5000` en tu navegador.

### Ejecución con Docker

1. Asegúrate de tener Docker instalado en tu máquina.
2. Construye la imagen Docker ejecutando el siguiente comando en la raíz del proyecto: `docker build -t bayeta-fortuna .`
3. Ejecuta el contenedor Docker con el siguiente comando: `docker run -p 5000:5000 bayeta-fortuna`
4. Accede a `http://localhost:5000` en tu navegador.

## Endpoints

- `/`: Página principal con un saludo.
- `/frotar/<n_frases>`: Obtiene `n_frases` frases auspiciosas.

## Contribuciones

Para este gran proyecto ha colaborado mi gran amigo Rafael Ibáñez Durán!!

## Notas de la Versión

### Versión 1.0

- Saludo en la página principal.
- Frases auspiciosas en formato JSON.


### Version 2.0

- Mejoras en la presentación.
- Integración con Docker.

---

*Proyecto desarrollado como parte de la práctica de Puesta en Producción Segura "La Bayeta de la Fortuna".*

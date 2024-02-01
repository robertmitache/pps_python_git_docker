# La Bayeta de la Fortuna

La Bayeta de la Fortuna es una aplicación web sencilla que proporciona frases auspiciosas de manera aleatoria cada vez que accedes a la página.

## Funcionalidades

- Muestra un saludo simple en la página principal.
- Proporciona frases auspiciosas en la ruta `/frotar/<n_frases>` en formato JSON.

## Ejecución con Docker

1. Asegúrate de tener Docker instalado en tu máquina.
2. Crea una red de Docker ejecutando `docker network create bayeta-network`.
3. Construye la imagen Docker ejecutando el siguiente comando en la raíz del proyecto: `docker build -t bayeta-fortuna .`
4. Ejecuta el contenedor de MongoDB en la red que acabas de crear con el siguiente comando: `docker run -d --name mongo-bayeta --network bayeta-network mongo:latest`. Esto iniciará el contenedor de MongoDB en segundo plano y lo conectará a la red de Docker.
5. Ejecuta el contenedor de la aplicación en la misma red con el siguiente comando: `docker run -d --name bayeta-app -p 5000:5000 --network bayeta-network bayeta-fortuna`. Esto iniciara la aplicación y la conectará al contenedor de MongoDB.
6. Accede a `http://localhost:5000` en tu navegador.


## Endpoints

- `/`: Página principal con un saludo.
- `/frotar/<n_frases>`: Obtiene `n_frases` frases auspiciosas.

## Contribuciones

Para este gran proyecto ha colaborado mi gran amigo Rafael Ibáñez Durán!!

## Notas de la Versión

### Versión 1.4

- Implementación de base de datos MongoDB para almacenar y recuperar frases auspiciosas.
- Mejoras en la gestión de redes Docker para facilitar la escalabilidad y la integración con servicios externos.

*Proyecto desarrollado como parte de la práctica de Puesta en Producción Segura "La Bayeta de la Fortuna".*

# Flask Hello World Docker Application

A minimal Flask application that returns **"Hello World"** on the root (`/`) endpoint, containerized with Docker.

## Prerequisites

* Docker installed

## Build the Docker image

From the project directory, run:

```bash
docker build -t flask-hello .
```

## Run the container

```bash
docker run -d -p (host-port):5000 --name flask-app flask-hello
```

## Verify the application

Open your browser and visit:

```
http://localhost:(host-port)/
```

or test it from the terminal:

```bash
curl http://localhost:(host-port)/
```

or test it from the container itself:

```bash
docker exec -it flask-app curl http://localhost:5000/
```

Expected output:

```
Hello World
```

## Stop the container

```bash
docker stop flask-app
```

## Remove the container

```bash
docker rm flask-app
```


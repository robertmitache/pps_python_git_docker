# Fase de resolución de dependencias
FROM python:3.11.7-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

# Fase de ejecución
FROM python:3.11.7-slim AS runner
WORKDIR /app
COPY --from=builder /app/venv /app/venv
COPY . .
CMD ["venv/bin/python", "app.py"]

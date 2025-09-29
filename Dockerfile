# Dockerfile
FROM python:3.10-slim AS builder
WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Final image
FROM python:3.10-slim
WORKDIR /app

# Copy installed packages from builder (we re-install to keep image simple)
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app
ENV MODEL_PATH=/app/models/model.joblib
EXPOSE 8000

# Use gunicorn for production-like server
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app", "--workers", "2", "--threads", "4"]

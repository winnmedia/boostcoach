FROM python:3.11-slim-bullseye

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y netcat-traditional && \
    pip install --no-cache-dir -r requirements.txt
RUN python3 -c "import alembic"

COPY alembic.ini .
COPY alembic alembic

COPY . .
COPY start.sh .
RUN chmod +x start.sh

CMD ["./start.sh"]

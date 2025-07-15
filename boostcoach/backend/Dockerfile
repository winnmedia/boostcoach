FROM python:3.11-slim-bullseye

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python3 -c "import alembic"

COPY alembic.ini .
COPY alembic alembic

COPY . .
COPY start.sh .
RUN chmod +x start.sh

CMD ["./start.sh"]

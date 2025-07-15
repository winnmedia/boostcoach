FROM python:3.11-slim-bullseye

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY start.sh .
RUN chmod +x start.sh

CMD ["./start.sh"]

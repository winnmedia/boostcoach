FROM python:3.11-slim-bullseye

WORKDIR /app

# Install Node.js and npm from NodeSource
RUN apt-get update && apt-get install -y curl &&     curl -fsSL https://deb.nodesource.com/setup_18.x | bash - &&     apt-get install -y nodejs &&     ln -s /usr/bin/python3 /usr/bin/python

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Prisma CLI
COPY package.json package-lock.json ./
RUN npm install --verbose

COPY . .
COPY start.sh .
RUN chmod +x start.sh

CMD ["./start.sh"]

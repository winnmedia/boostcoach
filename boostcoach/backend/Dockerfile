# Stage 1: Build dependencies
FROM python:3.11-slim-bullseye AS builder

WORKDIR /app

# Install Node.js and npm from NodeSource
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    ln -s /usr/bin/python3 /usr/bin/python

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js dependencies
COPY package.json package-lock.json ./
RUN npm install --verbose

# Stage 2: Runtime image
FROM python:3.11-slim-bullseye

WORKDIR /app

# Install Node.js and npm from NodeSource (runtime)
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    ln -s /usr/bin/python3 /usr/bin/python

# Install Python dependencies in runtime stage
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js production dependencies in runtime stage
COPY package.json package-lock.json ./ 
RUN npm install --production

# Copy prisma CLI binary and engines
COPY --from=builder /app/node_modules/.bin/prisma /usr/local/bin/prisma
COPY --from=builder /app/node_modules/@prisma/engines /app/node_modules/@prisma/engines



COPY . .
COPY start.sh .
RUN chmod +x start.sh

CMD ["./start.sh"]

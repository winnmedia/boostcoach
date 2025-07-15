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

# Install Prisma CLI and Node.js dependencies
COPY package.json package-lock.json ./
RUN npm install --verbose
RUN npm install prisma # Install prisma locally

# Stage 2: Runtime image
FROM python:3.11-slim-bullseye

WORKDIR /app

# Copy only necessary Node.js related files from builder stage
COPY --from=builder /app/node_modules /app/node_modules
COPY --from=builder /usr/bin/node /usr/bin/node
COPY --from=builder /usr/bin/npm /usr/bin/npm

# Copy prisma CLI binary
COPY --from=builder /app/node_modules/.bin/prisma /usr/local/bin/prisma
COPY --from=builder /app/node_modules/@prisma/engines /app/node_modules/@prisma/engines

# Install Python dependencies in runtime stage
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create python symlink in runtime stage
RUN ln -s /usr/bin/python3 /usr/bin/python

COPY . .
COPY start.sh .
RUN chmod +x start.sh

CMD ["./start.sh"]

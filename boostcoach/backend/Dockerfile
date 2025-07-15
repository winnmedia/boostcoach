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

# Stage 2: Runtime image
FROM python:3.11-slim-bullseye

WORKDIR /app

# Copy only necessary files from builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /app/node_modules /app/node_modules
COPY --from=builder /usr/bin/node /usr/bin/node
COPY --from=builder /usr/bin/npm /usr/bin/npm
COPY --from=builder /usr/bin/npx /usr/bin/npx
COPY --from=builder /usr/bin/python /usr/bin/python # Symlink

COPY . .
COPY start.sh .
RUN chmod +x start.sh

CMD ["./start.sh"]

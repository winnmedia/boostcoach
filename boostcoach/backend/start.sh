#!/bin/bash

set -e

# Ensure DATABASE_URL is set for Prisma
# Railway injects DATABASE_URL, so we just need to make sure it's available to npx commands
# If DATABASE_URL is not set, this will cause an error, which is intended.
if [ -z "$DATABASE_URL" ]; then
  echo "Error: DATABASE_URL environment variable is not set."
  exit 1
fi

# Run Prisma Migrations
echo "Running Prisma Migrations..."
npx prisma migrate deploy

# Generate Prisma Client
echo "Generating Prisma Client..."
npx prisma generate

# Start Uvicorn server
echo "Starting Uvicorn server..."
uvicorn main:app --host 0.0.0.0 --port 3000
